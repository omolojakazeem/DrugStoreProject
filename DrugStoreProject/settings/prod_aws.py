from .base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'psm_mydb',
        'USER': 'psm_myadmin',
        'PASSWORD': 'psm_admin_pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
