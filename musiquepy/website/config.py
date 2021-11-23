from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

"""Flask configuration."""
FLASK_ENV = environ.get('FLASK_ENV')
DEBUG = True
TESTING = False

STATIC_FOLDER = 'static'
TEMPLATES_FOLDER = 'templates'

SESSION_TYPE = environ.get('SESSION_TYPE')
SECRET_KEY = environ.get('SECRET_KEY')
SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
SESSION_FILE_DIR = '.flask_session'

ASSETS_DEBUG = False
ASSETS_AUTO_BUILD = True

DB_FILEPATH = 'musiquepy_db.sqlite'