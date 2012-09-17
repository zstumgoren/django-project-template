from config.base.settings import *

INTERNAL_IPS=('127.0.0.1')

ROOT_URLCONF = 'config.prod.urls'

WSGI_APPLICATION = 'config.prod.{{ project_name }}_wsgi.application'

# DB settings stored in a file outside version control
try:
    from config.prod.db_settings import DATABASES
except ImportError:
    pass

INSTALLED_APPS += (
    #'debug_toolbar',
    'django_extensions',
    'south',
    'test_utils',
)
