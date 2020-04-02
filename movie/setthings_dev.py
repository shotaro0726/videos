from movie.setthings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

Logging = {
    'version':1,
    'disable_existing':False,
    'loggers':{
        'django':{
            'handlers':['console'],
            'level':'INFO',
        },
        'movie_site':{
            'handlers':['console'],
            'level':'DEBUG',
        },
    },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev'
        },
    },
    'formatters':{
        'dev':{
            'format':'\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(Lineno)d)',
                '%(message)s'
            ])
        },
    }
}