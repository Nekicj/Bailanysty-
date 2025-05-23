# Bailanysty

A Django-based social media web application that enables users to connect, share posts, and interact with each other through a modern web interface.

## Technologies Used

- Python 3.x
- Django 5.2.1
- Django REST Framework 3.16.0
- PostgreSQL
- Additional key packages:
  - django-cors-headers 4.7.0 (for handling Cross-Origin Resource Sharing)
  - Pillow 11.2.1 (for image processing)
  - gunicorn 23.0.0 (for production deployment)
  - whitenoise 6.9.0 (for static files handling)
  - django-crispy-forms 2.0 (for form rendering)
  - python-dotenv 1.0.0 (for environment variables)

## Project Structure

```
ailanysta/
├── ailanysta/          # Main project configuration
├── posts/             # Posts management application
├── users/             # Custom user management
├── notifications/     # Notification system
├── media/            # User-uploaded files
├── static/           # Static files (CSS, JS, images)
├── staticfiles/      # Collected static files for production
└── templates/        # HTML templates
```

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- PostgreSQL
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd ailanysta
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```


4. Run migrations:
```bash
python manage.py migrate
```

5. Collect static files:
```bash
python manage.py collectstatic
```

## Running the Application

6. Start the development server:
```bash
python manage.py runserver
```

2. Access the application at:
- Main application: http://localhost:8000
- Admin interface: http://localhost:8000/admin
- Login page: http://localhost:8000/accounts/login/

## Features

- **Custom User Authentication**
  - Custom user model
  - Login/Registration system
  - User profiles with profile pictures

- **Post Management**
  - Create, read, update, and delete posts
  - Media file upload support
  - Interactive user interface

- **Notification System**
  - Real-time notifications
  - User interaction tracking

- **REST API Support**
  - Django REST Framework integration
  - API endpoints for posts and user data
  - CORS support for frontend integration

## Development Configuration

### Debug Settings
Debug mode is enabled by default in development. Configure it using the `DEBUG` environment variable.

### Static and Media Files
- Static files are served using WhiteNoise
- Media files are stored in the `media/` directory
- Static files are collected to `staticfiles/`


3. Static files serving with WhiteNoise:
- Ensure `whitenoise.middleware.WhiteNoiseMiddleware` is in `MIDDLEWARE`
- Run `python manage.py collectstatic`
