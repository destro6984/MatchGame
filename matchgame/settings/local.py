from .base import *


ALLOWED_HOSTS = ['localhost','127.0.0.1']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'local_db',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }
MEDIA_URL = '/images/'
MEDIA_ROOT = 'static/images'
