# -*- coding: utf-8 -*-

########### TEST SETTINGS
from .base import *

# SECURITY
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['explicandolaweb.bienvenido.webfactional.com']

# DATABASE LOCAL
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.sqlite3',
        'NAME':     'memory',
        'USER':     '',
        'PASSWORD': '',
        'HOST': ''
    }
}
