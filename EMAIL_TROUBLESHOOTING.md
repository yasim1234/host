# Troubleshooting Email Sending Issues

This guide will help you fix the "Application accepted but there was an error sending the offer letter" error.

## Step 1: Update Your Email Settings

The most common cause of this error is that you're still using placeholder values in your email settings. Open your `job_finder/settings.py` file and update the following settings:

```python
# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-actual-email@gmail.com'  # Replace with your actual Gmail address
EMAIL_HOST_PASSWORD = 'your-actual-app-password'  # Replace with your Gmail app password
DEFAULT_FROM_EMAIL = 'your-actual-email@gmail.com'  # Replace with your actual Gmail address
```

Replace:
- `your-actual-email@gmail.com` with your actual Gmail address (in both places)
- `your-actual-app-password` with the Gmail app password you generated

## Step 2: Generate a Gmail App Password

If you haven't already generated a Gmail app password:

1. Go to your Google Account settings: https://myaccount.google.com/
2. Click on "Security" in the left sidebar
3. Under "Signing in to Google," enable "2-Step Verification" if not already enabled
4. After enabling 2-Step Verification, go back to the Security page
5. Look for "App passwords" under "Signing in to Google"
6. Select "Mail" as the app and "Other" as the device (you can name it "Django")
7. Click "Generate"
8. Google will generate a 16-character password
9. Copy this password and use it as your `EMAIL_HOST_PASSWORD`

## Step 3: Test Your Email Settings

Run the test script to verify your email settings:

```bash
python test_email.py
```

Enter your email address when prompted. If everything is set up correctly, you should receive a test email.

## Step 4: Test the Offer Letter Functionality

Run the offer letter test script to verify that the offer letter functionality works:

```bash
python test_offer_letter.py
```

This script will create a test application and attempt to send an offer letter.

## Step 5: Restart Your Django Server

After updating the settings, restart your Django development server:

```bash
python manage.py runserver
```

## Common Issues and Solutions

### 1. "Invalid credentials" error

**Solution**: Double-check your app password and make sure you've copied it correctly. The app password should be 16 characters long.

### 2. "SMTP connection failed" error

**Solution**: Check your internet connection and make sure your firewall isn't blocking the connection.

### 3. "Recipient refused" error

**Solution**: Make sure the recipient email address is correct.

### 4. "SSL/TLS error" error

**Solution**: Make sure `EMAIL_USE_TLS = True` is set in your settings.

### 5. Gmail security alerts

**Solution**: You might receive a security alert from Google. Click "Yes, it's me" to allow the connection.

### 6. "Less secure app access" error

**Solution**: Gmail may block "less secure app access." To fix this, either:
- Enable "Less secure app access" in your Google Account settings (not recommended)
- Use an App Password (recommended)

### 7. "Rate limit exceeded" error

**Solution**: Gmail has rate limits for sending emails. If you're sending too many emails in a short period, you may hit this limit. Wait a while and try again.

## Using Console Backend for Testing

If you're having trouble with the SMTP backend, you can temporarily switch to the console backend for testing:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

This will print emails to the console instead of sending them, which can be helpful for debugging.

## Checking Email Templates

Make sure your email templates are in the correct location:
- `jobs/templates/jobs/email/offer_letter.html`
- `jobs/templates/jobs/email/offer_letter.txt`

If these files don't exist or are in the wrong location, the email sending will fail.

## Checking for Typos in Email Addresses

Make sure there are no typos in the email addresses in your settings or in the applicant's email address.

## Checking for Special Characters in Passwords

If your app password contains special characters, make sure they're properly escaped in your settings.

## Using Environment Variables

For better security, you can use environment variables instead of hardcoding your email credentials:

1. Install python-dotenv: `pip install python-dotenv`
2. Create a `.env` file in your project root:
   ```
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   DEFAULT_FROM_EMAIL=your-email@gmail.com
   ```
3. Update your settings.py:
   ```python
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   
   EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
   EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
   DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
   ```
4. Add `.env` to your `.gitignore` file to prevent it from being committed 