"""
Django settings for edm project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import django.conf.global_settings as DEFAULTS

IP_USER_HEADER_FIELD = 'X-TheUltimateReal-IP'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@&5db4oyb6sjikzxona!8l8crhpvf=#xc90$@h$j5l)4&@%)&g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
CRISPY_TEMPLATE_PACK = 'bootstrap3'
SITE_ID = 1
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.webdesign',
    'social.apps.django_app.default',
    'south',
    'djangobower',
    'django_extensions',
    'taggit',
    'account',
    'crispy_forms',
    'main',
    'edmmusic',
    'edmproject',
    'edmpurchase',
    'edmreview',
    'edmupload',
    'edmuser',
)

MIDDLEWARE_CLASSES = (
    'edmuser.middleware.UserIpAddressMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'edmuser.middleware.UserSessionMiddleware',
    'edmuser.middleware.UserUrlTrackerMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
)

ROOT_URLCONF = 'edm.urls'

WSGI_APPLICATION = 'edm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'edm',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 3306
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True

SOCIAL_AUTH_GITHUB_KEY = 'fe0963d1e725d67f2ce7'
SOCIAL_AUTH_GITHUB_SECRET = '5568ebb7b5e327f02a3e028f7c3cd1ba3a3967f9'

AUTHENTICATION_BACKENDS = DEFAULTS.AUTHENTICATION_BACKENDS + (
    'social.backends.github.GithubOAuth2',
    'social.apps.django_app.utils.BackendWrapper',
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULTS.TEMPLATE_CONTEXT_PROCESSORS + (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'account.context_processors.account',
    'edmproject.context_processors.categories',
)

TEMPLATE_LOADERS = DEFAULTS.TEMPLATE_LOADERS + (
    'django.template.loaders.app_directories.Loader',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_FINDERS = DEFAULTS.STATICFILES_FINDERS + (
    'djangobower.finders.BowerFinder',
)

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')
BOWER_INSTALLED_APPS = (
    'jquery',
    'lodash',
    'bootstrap',
)