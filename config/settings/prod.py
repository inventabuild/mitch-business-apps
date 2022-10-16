import django_on_heroku
from decouple import config

from config.settings.dev import DEBUG

from .base import *

SECRET_KEY = config('SECRET-KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'mitch-business-apps.herokuapp.com'
]