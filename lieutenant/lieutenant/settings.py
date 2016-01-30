"""
Django settings for lieutenant project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'he&$oe$(3va(8la@_!8*3&b)t(3ry0k2bo*7$&$%p&qy&4fr#8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    # Required by `allauth` template tags
    'django.core.context_processors.request',

    # `allauth` specific context processors
    'allauth.account.context_processors.account',
    'dealer.contrib.django.context_processor',
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'widget_tweaks',
    'allauth',
    'allauth.account',
    'rest_framework',
    'taggit',
    'favorites',
    'taggit_serializer',
    'randomslugfield',
    'entries',
    'tags',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'dealer.contrib.django.Middleware',
)

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
]

SITE_ID = 1

ROOT_URLCONF = 'lieutenant.urls'

WSGI_APPLICATION = 'lieutenant.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':     os.environ.get("LIEUTENANT_DB_NAME", 'lieutenant'),
        'USER':     os.environ.get("LIEUTENANT_DB_USER", 'django_lieutenant'),
        'PASSWORD': os.environ.get("LIEUTENANT_DB_PASSWORD", ''),
        'HOST':     os.environ.get("LIEUTENANT_DB_HOST", 'localhost'),
        'PORT':     os.environ.get("LIEUTENANT_DB_PORT", ''), # Set to empty string for default
    }
    #'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME':     os.environ.get(BASE_DIR, 'db.sqlite3'),
    #}
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Location where the collectstatic command will place static files
STATIC_ROOT = '/home/lieutenant/static'
