from .common import *
from .partials.util import get_secret

DEBUG = False

# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

ALLOWED_HOSTS = ['.gaviriafajardo.com', '.gaviriafajardo.co', '.gaviriafajardo.com.co']
SECRET_KEY = get_secret('DJANGO_SECRET_KEY')

if get_secret('DATABASE_URL'):
    import dj_database_url

    DATABASES = {
        'default': dj_database_url.config()
    }
else:
    POSTGRES_DB = get_secret('POSTGRES_DB')
    POSTGRES_USER = get_secret('POSTGRES_USER')
    POSTGRES_PASSWORD = get_secret('POSTGRES_PASSWORD')

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': POSTGRES_DB,
            'USER': POSTGRES_USER,
            'PASSWORD': POSTGRES_PASSWORD,
            'HOST': 'db',
            'PORT': 5432,
        }
    }


WEBPACK_LOADER['DEFAULT'].update({
    'BUNDLE_DIR_NAME': 'dist/',  # must end with slash
    'STATS_FILE': os.path.join(BASE_DIR, 'webpack-production-stats.json'),
})

# Email Config
"""
EMAIL_PASSWORD = get_secret('EMAIL_PASSWORD')
EMAIL_HOST = 'smtp.gaviriafajardo.com'
EMAIL_HOST_USER = 'gaviriafajardo'
EMAIL_HOST_PASSWORD = EMAIL_PASSWORD
"""
