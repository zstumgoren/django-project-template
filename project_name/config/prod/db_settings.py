# Default to sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', #'django.db.backends.postgresql_psycopg2',
        'NAME': os.path.join(PROJECT_ROOT, '{{ project_name }}.db'),
        'USER':  '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
