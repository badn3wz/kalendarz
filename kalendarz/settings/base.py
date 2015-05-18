"""
Django settings for kalendarz project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qwerty'

# SECURITY WARNING: don't run with debug turned on in production!
if not (os.environ.get("HOME") == '/home/qwe'):
    DEBUG = False
else:
    DEBUG = True

THUMBNAIL_DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = (
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'djrill',
    #'allauth.socialaccount'
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cal',
    'playerprofile',
    'galeria',
    'sorl.thumbnail',
    'permission',
    'debug_toolbar',
    'braces',
    'bootstrap3',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'audit_log.middleware.UserLoggingMiddleware',
)

ROOT_URLCONF = 'kalendarz.urls'

WSGI_APPLICATION = 'kalendarz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases



# if 'DEVELOPMENT' in os.environ:
#   DATABASES = {
#       'default': {
#           'ENGINE': 'django.db.backends.postgresql_psycopg2',
#           'NAME': 'dbname',
#           'USER': 'username',
#           'PASSWORD': 'passwd',
#           'HOST': 'localhost',
#           'PORT': '',
#       }
#   }
# else:
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Absolute path to the media directory
# STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__),'static'),)
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

    #django-permission
    'permission.backends.PermissionBackend',
)

CSRF_COOKIE_NAME = 'csrf_token'

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_SUBJECT_PREFIX = ""
ACCOUNT_PASSWORD_MIN_LENGTH = 8
ACCOUNT_USERNAME_REQUIRED = True

LOGIN_REDIRECT_URL = 'index'


DEFAULT_FROM_EMAIL = 'admin@intactilis.pl'

EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
MANDRILL_API_KEY = ""
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'



STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

THUMBNAIL_COLORSPACE = None 

THUMBNAIL_PRESERVE_FORMAT = True 


BOOTSTRAP3 = {

    # The URL to the jQuery JavaScript file
    'jquery_url': '/static/js/jquery.min.js',

    # The Bootstrap base URL
    'base_url': '/static/',

    # The complete URL to the Bootstrap CSS file (None means derive it from base_url)
    'css_url': '/static/css/navbar.css',

    # The complete URL to the Bootstrap CSS file (None means no theme)
    'theme_url': '/static/css/slate.css',
    #'theme_url': 'http://bootswatch.com/slate/bootstrap.min.css',
    #'theme_url': 'http://bootswatch.com/superhero/bootstrap.min.css',

    # The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
    'javascript_url': None,

    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap3.html)
    'javascript_in_head': False,

    # Include jQuery with Bootstrap JavaScript (affects django-bootstrap3 template tags)
    'include_jquery': False,

    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-2',

    # Field class to use in horizontal forms
    'horizontal_field_class': 'col-md-4',

    # Set HTML required attribute on required fields
    'set_required': False,

    # Set placeholder attributes to label if no placeholder is provided
    'set_placeholder': True,

    # Class to indicate required (better to set this in your Django form)
    'required_css_class': '',

    # Class to indicate error (better to set this in your Django form)
    'error_css_class': 'has-error',

    # Class to indicate success, meaning the field has valid input (better to set this in your Django form)
    'success_css_class': 'has-success',


}