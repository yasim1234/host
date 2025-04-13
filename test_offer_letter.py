import os
import django
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_finder.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from jobs.models import JobPosting, JobApplication, UserProfile
from jobs.utils import send_offer_letter

def test_offer_letter():
    """Test the offer letter functionality by creating a test application and sending an offer letter."""
    print("Testing offer letter functionality...")
    
    # Check if we have placeholder email values
    if settings.EMAIL_HOST_USER == 'your-email@gmail.com' or settings.EMAIL_HOST_PASSWORD == 'your-app-password':
        print("ERROR: You need to update your email settings in the .env file with your actual Gmail credentials.")
        print("Please follow the instructions in EMAIL_TROUBLESHOOTING.md to set up your email settings.")
        return
    
    # Try to find an existing accepted application
    try:
        application = JobApplication.objects.filter(status='ACCEPTED').first()
        if application:
            print(f"Found an existing accepted application: {application}")
        else:
            print("No existing accepted applications found. Creating test data...")
            
            # Create test user if it doesn't exist
            test_user, created = User.objects.get_or_create(
                username='test_applicant',
                defaults={
                    'email': 'test_applicant@example.com',
                    'first_name': 'Test',
                    'last_name': 'Applicant'
                }
            )
            if created:
                test_user.set_password('testpassword123')
                test_user.save()
                print(f"Created test user: {test_user.username}")
            
            # Create user profile if it doesn't exist
            profile, created = UserProfile.objects.get_or_create(
                user=test_user,
                defaults={
                    'is_applicant': True,
                    'is_company': False
                }
            )
            if created:
                profile.save()
                print(f"Created user profile for {test_user.username}")
            
            # Create test job posting if it doesn't exist
            job, created = JobPosting.objects.get_or_create(
                title='Test Job',
                defaults={
                    'company_name': 'Test Company',
                    'description': 'This is a test job posting',
                    'requirements': 'Test requirements',
                    'location': 'Test Location',
                    'pay_rate': 'Test Pay Rate',
                    'hours_per_week': 40,
                    'application_deadline': '2023-12-31',
                    'is_active': True,
                    'is_featured': False
                }
            )
            if created:
                job.save()
                print(f"Created test job posting: {job.title}")
            
            # Create test application
            application = JobApplication.objects.create(
                job=job,
                applicant=test_user,
                status='ACCEPTED',
                cover_letter='This is a test cover letter'
            )
            print(f"Created test application: {application}")
    
        # Try to send the offer letter
        print(f"Attempting to send offer letter for application: {application}")
        try:
            send_offer_letter(application)
            print("Offer letter sent successfully!")
        except Exception as e:
            print(f"Error sending offer letter: {e}")
            print("\nTroubleshooting tips:")
            print("1. Make sure you've updated the .env file with your actual Gmail credentials")
            print("2. Verify that you've generated an App Password from your Google Account")
            print("3. Check that 2-Step Verification is enabled on your Google Account")
            print("4. Ensure your Gmail address and App Password are correct")
            print("5. Check your internet connection")
            print("6. Verify that the email templates exist in the correct location")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_offer_letter() 