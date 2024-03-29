# -*- encoding: utf-8 -*-

########### BASE SETTINGS

import os
from unipath import Path
PROJECT_DIR = Path(__file__).ancestor(3)
MEDIA_ROOT = PROJECT_DIR.child("media")
STATIC_ROOT = PROJECT_DIR.child("static")

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

TEMPLATE_DIRS = (
    PROJECT_DIR.child("templates"),
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["KEY_DJANGO"]

# Application definition
INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.sites',
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
    'taggit',
    'disqus',

    # ExplicandoLaWeb
    'articulos',
    'categorias',
    'tutoriales',
    'cursos',
    'blog',
    'perfiles',
    'web',
)

DISQUS_API_KEY = os.environ["DISQS_KEY"]
DISQUS_WEBSITE_SHORTNAME = 'explicandolaweb'

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
    'web.context_processors.categorias_tutoriales',
    'web.context_processors.ultimos_tutoriales',
    'web.context_processors.ultimos_capitulos',
    'web.context_processors.ultimos_post',
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
