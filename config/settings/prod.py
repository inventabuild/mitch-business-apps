from turtle import st
import django_on_heroku
from decouple import config

from config.settings.dev import DEBUG

from .base import *

SECRET_KEY = config('SECRET-KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'mitch-business-apps.herokuapp.com'
]

DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
    'version': 1,
	'disable_existing_loggers': False,
	'formatters':{
	    'verbose': {
	        'format' : "[%(asctime}s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
	        'datefmt' : "%d/%b/%Y %H:%M:%S"
	    },
	    'simple': {
	        'format': '%(levelname)s %(message)s'
	    },
	},
	'handlers': {
	    'console': {
	        'level': 'DEBUG',
	        'class': 'logging.StreamHandler',
	    },
	},
	'loggers': {
	    'MYAPP': {
	        'handlers': ['console'],
	        'level': 'DEBUG',
	    },
	}
}


#Heroku Settings
django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']