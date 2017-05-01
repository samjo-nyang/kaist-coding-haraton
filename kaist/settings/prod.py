from .common import *

import pymysql
pymysql.install_as_MySQLdb()

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ['storages']

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.mysql'),
        'HOST': os.environ.get('DB_HOST', ''),
        'NAME': os.environ.get('DB_NAME', ''),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'PORT': os.environ.get('DB_PORT', 3306),
    },
}
STATICFILES_STORAGE = 'kaist.storages.StaticAzureStorage'
DEFAULT_FILE_STORAGE = 'kaist.storages.MediaAzureStorage'

AZURE_ACCOUNT_NAME = os.environ.get('AZURE_ACCOUNT_NAME', '')
AZURE_ACCOUNT_KEY = os.environ.get('AZURE_ACCOUNT_KEY', '')
AZURE_CONTAINER = os.environ.get('AZURE_CONTAINER', '')
AZURE_MEDIA_CONTAINER = os.environ.get('AZURE_MEDIA_CONTAINER', '')
