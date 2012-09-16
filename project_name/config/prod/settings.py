from config.base.settings import *

INTERNAL_IPS=('127.0.0.1')

ROOT_URLCONF = 'config.prod.urls'

WSGI_APPLICATION = 'config.prod.{{ project_name }}_wsgi'

# Default to sqlite
DATABASES = {
    'default': {
        'ENGINE': os.path.join(PROJECT_ROOT, '{{ project_name }}.db'), #'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER':  '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# If we use anything other than sqlite, move database settings in 
# 'db_settings.py' file outside of version control
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
