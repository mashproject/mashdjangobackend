from base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w^%2_j5b^5zvq9#9d66ed=3yf(jj4ax&bex_@^sh*6hhl!xyv9'

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mash_backend',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}
EMAIL_BACKEND = 'seacucumber.backend.SESBackend'
CELERY_DISABLE_RATE_LIMITS = False

TEMPLATE_DEBUG = False

AWS_ACCESS_KEY_ID = 'AKIAI3SX3OZAFCO6JGNQ'
AWS_SECRET_ACCESS_KEY = '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'
DEFAULT_EMAIL_SENDER = 'hello@mashglobal.org'