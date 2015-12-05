from base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w^%2_j5b^5zvq9#9d66ed=3yf(jj4ax&bex_@^sh*6hhl!xyv9'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'my.cnf'),
        },
    }
}
EMAIL_BACKEND = 'seacucumber.backend.SESBackend'
CELERY_DISABLE_RATE_LIMITS = False

TEMPLATE_DEBUG = False

AWS_ACCESS_KEY_ID = 'AKIAJA4N6SXSQRSVHJDQ'
AWS_SECRET_ACCESS_KEY = '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'
