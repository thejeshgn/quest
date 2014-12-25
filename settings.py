"""
Django settings for instavaani project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))
sys.path.insert(0, os.path.join(PROJECT_ROOT, '..','..',"app"))
sys.path.insert(0, os.path.join(PROJECT_ROOT, '..','..',"lib"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dpc)c$h^0+&q&m=tn&%ey0)-wa+c&)odp5bv*7x9u4df4ef#h_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'daterange_filter',
    'tracking',
    'bootstrap3',
    'south',
    'social_auth',
    'django_js_reverse',
    'quest'
)

MIDDLEWARE_CLASSES = (
    'social_auth.middleware.SocialAuthExceptionMiddleware',                  
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
"django.core.context_processors.request",
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages",
"django_mobile.context_processors.flavour",
"social_auth.context_processors.social_auth_by_type_backends"
    )

#TEMPLATE_LOADERS = (
#    'django_mobile.loader.Loader',
#)

ROOT_URLCONF = 'quest.urls'

WSGI_APPLICATION = 'quest.wsgi.application'



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

#USE_I18N = True

#USE_L10N = True

USE_TZ = False


DATE_INPUT_FORMATS=(
    '%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y', # '25-10-2006', '25/10/2006', '25/10/06'
    '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
)
DATETIME_INPUT_FORMATS=(
    '%d-%m-%Y %H:%M:%S',     # '2006-10-25 14:30:59'
    '%d-%m-%Y %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%d-%m-%Y %H:%M',        # '2006-10-25 14:30'
    '%d-%m-%Y',              # '2006-10-25'
    '%d/%m/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    '%d/%m/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    '%d/%m/%Y %H:%M',        # '10/25/2006 14:30'
    '%d/%m/%Y',              # '10/25/2006'
    '%d/%m/%y %H:%M:%S',     # '10/25/06 14:30:59'
    '%d/%m/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    '%d/%m/%y %H:%M',        # '10/25/06 14:30'
    '%d/%m/%y',              # '10/25/06'
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, "quest","static"),
    )



TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)


BOOTSTRAP3 = {

    # The URL to the jQuery JavaScript file
    'jquery_url': '//code.jquery.com/jquery.min.js',

    # The Bootstrap base URL
    'base_url': '//netdna.bootstrapcdn.com/bootstrap/3.3.1/',

    # The complete URL to the Bootstrap CSS file (None means derive it from base_url)
    'css_url': None,

    # The complete URL to the Bootstrap CSS file (None means no theme)
    'theme_url': '/static/bootstrap/css/bootstrap-yeti.min.css'

    }




# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
# # NOTE: Customize/Extend GoogleOAuth2Backend when roles needed from ldap
# AUTHENTICATION_BACKENDS = ('social_auth.backends.google.GoogleOAuth2Backend', 'customauth.restauthbackend.RestAuthBackEnd',)

# SOCIAL_AUTH_ENABLED_BACKENDS = ('google',)
# SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
# SOCIAL_AUTH_RAISE_EXCEPTIONS = False
# GOOGLE_OAUTH2_CLIENT_ID =''
# GOOGLE_OAUTH2_CLIENT_SECRET = ''
# GOOGLE_WHITE_LISTED_DOMAINS = ['quest.datameet.org']
# SOCIAL_AUTH_USER_MODEL = 'auth.User'


try:
    from prod_settings import *
except ImportError:
    #If production settings are present don't import local settings
    try:
        from dev_settings import *
    except ImportError:
        pass

