from .settings import *

import dj_database_url

DEBUG = False

DATABASES['default'] = dj_database_url.config('JAWSDB_URL')

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ALLOWED_HOSTS = ['127.0.0.1', 'gest-perso.herokuapp.com']

TEMPLATE_DEBUG = False

SECRET_KEY = 'SECRET_KEY'
