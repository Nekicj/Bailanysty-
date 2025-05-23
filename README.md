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

4. Create a `.env` file in the project root with the following variables:
```
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:password@localhost:5432/bailanysty
```

5. Set up the PostgreSQL database:
```bash
# Create a new PostgreSQL database named 'Bailanysty'
# Update database settings in settings.py or use environment variables
```

6. Run migrations:
```bash
python manage.py migrate
```

7. Collect static files:
```bash
python manage.py collectstatic
```

## Running the Application

1. Start the development server:
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

### Database Configuration
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Bailanysty',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Static and Media Files
- Static files are served using WhiteNoise
- Media files are stored in the `media/` directory
- Static files are collected to `staticfiles/`

## Production Deployment

1. Update settings for production:
- Set `DEBUG=False` in .env
- Configure proper `ALLOWED_HOSTS`
- Set secure SSL/HTTPS settings

2. Configure Gunicorn:
```bash
gunicorn ailanysta.wsgi:application
```

3. Static files serving with WhiteNoise:
- Ensure `whitenoise.middleware.WhiteNoiseMiddleware` is in `MIDDLEWARE`
- Run `python manage.py collectstatic`

4. Security considerations:
- Use strong SECRET_KEY
- Enable HTTPS
- Configure proper CORS settings
- Set secure cookie settings
- Use environment variables for sensitive data

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

