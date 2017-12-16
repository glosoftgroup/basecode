from .base import *

DEBUG = True
INSTALLED_APPS += ('django_extensions',)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'basecode',
        'USER': 'basecode',
        'ADMINUSER':'postgres',
        'PASSWORD': 'basecode',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}
