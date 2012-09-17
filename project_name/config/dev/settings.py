from config.base.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS=('127.0.0.1')

ROOT_URLCONF = 'config.dev.urls'

WSGI_APPLICATION = 'config.dev.{{ project_name }}_wsgi.application'

# DB settings stored in a file outside version control
try:
    from config.dev.db_settings import DATABASES
except ImportError:
    pass

# Test config tweaks/customizations
"""
if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE':'django.db.backends.sqlite3'}
    FIXTURE_DIRS = (
        PROJECT_ROOT + 'tests/fixtures',
    )
    SOUTH_TESTS_MIGRATE = False
"""

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
    'south',
    'test_utils',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    #'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    #'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
    #'HIDE_DJANGO_SQL': False,
    #'TAG': 'div',
}
