from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

"""Flask configuration."""

FLASK_ENV = 'development'
DEBUG = True
TESTING = False
SECRET_KEY = environ.get('SECRET_KEY')
SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
STATIC_FOLDER = 'static'
TEMPLATES_FOLDER = 'templates'