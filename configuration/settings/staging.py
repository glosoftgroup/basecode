# flake8:noqa
from .base import *

DEBUG = False

STAGE = "staging"

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'smsapp',
        'USER': 'smsappuser',
        'ADMINUSER':'postgres',
        'PASSWORD': 'Y904510P6cXM668mO96e',
        'HOST': 'smsapp-staging.cjlbpfelubaj.eu-west-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
