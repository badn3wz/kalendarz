"""
Django settings for kalendarz project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l)gk=^w@a+o4xv+npmmhcm%qd6ozzm)f0x4(1os^71*&jy#%*-'

# SECURITY WARNING: don't run with debug turned on in production!
if 'PRODUCTION' in os.environ:
	DEBUG = False
else:
	DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
	'django.contrib.sites',
	'allauth',
	'allauth.account',
	'djrill',
	#'allauth.socialaccount',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'cal',
	'debug_toolbar',
	'braces',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kalendarz.urls'

WSGI_APPLICATION = 'kalendarz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'caldb',
		'USER': 'qwe',
		'PASSWORD': 'qwe',
		'HOST': '',
		'PORT': '5432',
	}
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
	BASE_DIR + '/templates/',
)



TEMPLATE_CONTEXT_PROCESSORS = (
	"django.contrib.auth.context_processors.auth",
	# Required by allauth template tags
	"django.core.context_processors.request",
	# allauth specific context processors
	"allauth.account.context_processors.account",
	"allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
	# Needed to login by username in Django admin, regardless of `allauth`
	"django.contrib.auth.backends.ModelBackend",

	# `allauth` specific authentication methods, such as login by e-mail
	"allauth.account.auth_backends.AuthenticationBackend",
)


SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[Intactilis.pl]"
ACCOUNT_PASSWORD_MIN_LENGTH = 8
ACCOUNT_USERNAME_REQUIRED = True

LOGIN_REDIRECT_URL = 'index'


DEFAULT_FROM_EMAIL = 'admin@intactilis.pl'

EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
MANDRILL_API_KEY = "fu0fQiHR1GZavL8i7XXZGg"
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


if not os.environ.get("HOME") == '/home/qwe':
	# Parse database configuration from $DATABASE_URL
	import dj_database_url
	DATABASES['default'] = dj_database_url.config()


# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'





try:
	from local_settings import *
except ImportError as e:
	pass