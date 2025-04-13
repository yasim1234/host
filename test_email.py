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

def test_email():
    """Test email functionality by sending a test email."""
    print("Current email settings:")
    print(f"EMAIL_BACKEND: {settings.EMAIL_BACKEND}")
    print(f"EMAIL_HOST: {settings.EMAIL_HOST}")
    print(f"EMAIL_PORT: {settings.EMAIL_PORT}")
    print(f"EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}")
    print(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
    print(f"DEFAULT_FROM_EMAIL: {settings.DEFAULT_FROM_EMAIL}")
    print(f"EMAIL_HOST_PASSWORD: {'*' * len(settings.EMAIL_HOST_PASSWORD)} (hidden)")
    
    recipient_email = input("Enter your email address to receive the test email: ")
    
    try:
        send_mail(
            subject='Test Email from Job Finder',
            message='This is a test email to verify your email settings are working correctly.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient_email],
            fail_silently=False,
        )
        print(f"Test email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Error sending email: {e}")
        print("\nTroubleshooting tips:")
        print("1. Make sure you've updated the .env file with your actual Gmail credentials")
        print("2. Verify that you've generated an App Password from your Google Account")
        print("3. Check that 2-Step Verification is enabled on your Google Account")
        print("4. Ensure your Gmail address and App Password are correct")
        print("5. Check your internet connection")

if __name__ == "__main__":
    test_email() 