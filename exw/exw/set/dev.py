# -*- encoding: utf-8 -*-

########### DEVELOPMENT SETTINGS
from .base import *


# SECURITY
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']


# DATABASE LOCAL
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     os.environ["DB_NAME"],
        'USER':     os.environ["DB_USER"],
        'PASSWORD': os.environ["DB_PASS"],
        'HOST': ''
    }
}

INSTALLED_APPS += ('mockups', 'admin_honeypot',)
