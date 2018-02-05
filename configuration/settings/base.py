"""
Django settings for basecode project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import structlog
from loglib.logging import KeyValueRenderer

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1u=)fdv=lk=3sd&%zzmndj-e4tfp6z=jf=m9axx#v7@dkp6*x#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STAGE = "development"

ALLOWED_HOSTS = ['*']

ADMINS = (
    ('marete kent', 'maretekent@gmail.com'),

)

CORS_ORIGIN_ALLOW_ALL = True


# Application definition

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
)


THIRD_PARTY_APPS = (
    'gunicorn',
    'webpack_loader'
)

LOCAL_APPS = (
    'utilities',
    'loglib',
    'app_dir.api',
    'app_dir.core',
    'app_dir.modules.room',
)

INSTALLED_APPS = LOCAL_APPS + DEFAULT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'configuration.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR+'/app_dir/', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'configuration.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_DIR, 'static'))

STATIC_URL = '/static/'

MAIN_PROJECT = os.path.dirname(__file__)

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(MAIN_PROJECT, '../../app_dir/static/'),
)

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
]

S3_BUCKET = ''
S3_ACCESS_KEY = ''
S3_SECRET_KEY = ''

# MEDIA_URL = 'https://{0}/kenblest/kenblestkenya/attachments/'.format(conn.server_name())
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TIME_ZONE = 'Africa/Nairobi'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'environment': {
            '()': 'utilities.logging_filter.CustomFilter',
        },
    },
    'handlers': {
        'info_logfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'log/info.log',
            'formatter': 'verbose'
        },
        'debug_logfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'log/debug.log',
            'formatter': 'verbose'
        },
        'error_logfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'log/error.log',
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s module=%(module)s, '
                      'process_id=%(process)d, %(message)s'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'error_logfile'],
            'level': 'ERROR',
        },
        'api': {
            'handlers': ['console', 'debug_logfile'],
            'level': 'DEBUG',
        },
        'core': {
            'handlers': ['console', 'debug_logfile'],
            'level': 'DEBUG',
        },
        'celery': {
            'handlers': ['console', 'error_logfile'],
            'level': 'ERROR',
            'propagate': True
        },
        'app_dir': {
            'handlers': ['console', 'debug_logfile'],
            'level': 'DEBUG',
            'propagate': False
        },
        'utilities': {
            'handlers': ['console', 'debug_logfile'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

structlog.configure(
    logger_factory=structlog.stdlib.LoggerFactory(),
    processors=[
        structlog.processors.UnicodeEncoder(),
        KeyValueRenderer(),
    ]
)

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# api key that Console needs to use to call Hermes-sms
DEFAULT_CUSTOM_API_KEY = 'B+XXazAET/ZGVmYXVsdHN0cm9uZ2tleWZvcnRoZWFwaQ=='

# broker url
BROKER_USE_SSL = False
BROKER_URL = "amqp://guest:guest@rabbitmq:5672//"

# celery configs

CELERY_ROUTES = {
    'tasks.longtime_add': {'queue': 'longtime_add'}
}


CELERY_ENABLE_REMOTE_CONTROL = True
BROKER_HEARTBEAT = 10
CELERYD_MAX_TASKS_PER_CHILD = 100

# webpack settings
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(PROJECT_DIR, 'webpack-stats.json'),
    }
}