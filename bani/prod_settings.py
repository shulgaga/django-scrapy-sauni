from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-7)+aslkdj01293lo**3794yfh7)qrwre^qh5'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '213.189.221.92']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bani',
        'USER': 'tommy',
        'PASSWORD': '11223344',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]