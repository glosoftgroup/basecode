from configuration.settings.development import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'basecode',
        'USER': 'basecode',
        'PASSWORD': 'basecode',
        'HOST': 'db',
        'PORT': '5432',
    }
}
