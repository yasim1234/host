# Part-Time Job Finder for Students

A web application that connects students with flexible, part-time employment opportunities tailored to their academic schedules and skill sets.

## Features

- User registration and authentication for both students and employers
- Profile management with skills, availability, and contact information
- Job posting and management for employers
- Advanced job search and filtering
- Job application system
- Review system for both employers and students
- Responsive design for all devices

## Technologies Used

- Django 5.1.5
- Bootstrap 5
- SQLite (default database)
- Pillow for image handling
- Django Crispy Forms

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd part-time-job-finder
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your web browser

## Usage

### For Students
1. Register for a student account
2. Complete your profile with skills and availability
3. Browse and search for jobs
4. Apply to jobs that match your schedule
5. Track your applications
6. Leave reviews for employers

### For Employers
1. Register for an employer account
2. Create and manage job postings
3. Review applications from students
4. Accept or reject applications
5. Leave reviews for students

## Project Structure

```
part-time-job-finder/
├── jobs/                   # Main application
│   ├── migrations/        # Database migrations
│   ├── templates/        # HTML templates
│   ├── forms.py         # Form definitions
│   ├── models.py        # Database models
│   ├── urls.py          # URL configurations
│   └── views.py         # View functions
├── job_finder/           # Project settings
├── manage.py            # Django management script
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 