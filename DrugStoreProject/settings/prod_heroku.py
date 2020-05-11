import django_heroku

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['infinite-cove-35911.heroku.com']


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

django_heroku.settings(locals())