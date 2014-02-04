# -*- coding: utf-8 -*-

########### DEPLOY SETTINGS
from .base import *
import os

# SECURITY
DEBUG = False
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['explicandolaweb.com']

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
