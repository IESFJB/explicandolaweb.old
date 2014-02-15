# -*- coding: utf-8 -*-

#import os
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from unipath import Path
PROJECT_DIR = Path(__file__).ancestor(2)
MEDIA_ROOT = PROJECT_DIR.child("media")
STATIC_ROOT = PROJECT_DIR.child("static")

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    PROJECT_DIR.child("templates"),
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kt^((_@nf&!1hcd9v17^!@y&u3jq(nm==u8sb&porchv-qzl-6'


# Application definition
INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'tinymce',
    'sorl.thumbnail',
    'mce_filebrowser',
    'mockups',
    'taggit',

    # ExplicandoLaWeb
    'web',
    'categorias',
    'articulos',
    'cursos',
    'blog',
    'perfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    'web.context_processors.menu',
    'web.context_processors.categorias_articulos',
    'web.context_processors.categorias_cursos',
    'web.context_processors.ultimos_articulos',
)

ROOT_URLCONF = 'exw.urls'
WSGI_APPLICATION = 'exw.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'Europe/Madrid'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# TinyMCE
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'height': '500px',
    'width': '100%',

    'file_browser_callback': 'mce_filebrowser',
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True

#Fin de base.py



# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#     'django.contrib.staticfiles.finders.FileSystemFinder',
# )


# Configuracion del envio de emails
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 25
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = False

# Django Social Auth
# AUTHENTICATION_BACKENDS = (
    # 'social_auth.backends.twitter.TwitterBackend',
    # 'social_auth.backends.facebook.FacebookBackend',
    # 'social_auth.backends.google.GoogleOAuth2Backend',
    # 'django.contrib.auth.backends.ModelBackend',
# )

# TWITTER_CONSUMER_KEY        = 'drhXnJ6HHdCyr115UFhA'
# TWITTER_CONSUMER_SECRET     = 'OSK3jjxI3YjAWE2lor7BaPaoCO2r9g2V87E6oH2otGY'
# FACEBOOK_APP_ID             = ''
# FACEBOOK_API_SECRET         = ''
# GOOGLE_OAUTH2_CLIENT_ID     = ''
# GOOGLE_OAUTH2_CLIENT_SECRET = ''

# -*- coding: utf-8 -*-

# settings/local.py

# SECURITY
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['explicandolaweb.bienvenido.webfactional.com']

# EMAIL SERVER
#EMAIL_HOST = "localhost"
#EMAIL_PORT = 1025

# Database

# DATABASE LOCAL
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     'explicandolaweb',
        'USER':     'explicandolaweb',
        'PASSWORD': 'explicandolaweb',
        'HOST': ''
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': Path(PROJECT_DIR+'/bd.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'exw',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }
