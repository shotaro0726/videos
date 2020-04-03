from .settings_common import *

DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

STATIC_URL = '/usr/share/nginx/html/static'
MEDIA_URL = '/usr/share/nginx/html/media'

AWS_SES_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY_ID')
AES_SES_SECRET_ACCESS_KEY = os.environ.get('AWS_SES_SECRET_ACCESS_KEY')
EMAIL_BACKEND = 'django_ses.SESBackend'

Logging = {
    'version': 1,
    'disable_existing': False,

    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'movie_site': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'prod',
            'when': 'D',
            'interval': 1,
            'backupCount':7,
        },
    },
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(Lineno)d)',
                '%(message)s'
            ])
        },
    }
}
