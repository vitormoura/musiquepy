from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

"""Flask configuration."""
FLASK_ENV = environ.get('FLASK_ENV')
DEBUG = True
TESTING = False