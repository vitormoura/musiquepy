from logging.config import dictConfig
import os

from flask import Flask
from flask.helpers import get_root_path
from flask_session import Session
from flask_assets import Environment, Bundle 

assets = Environment()
sess = Session()

 
def create_app(test_config=None):

    # configure default logging
    _config_logging()

    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)

    if test_config is None:
       # config_file_path = os.path.join(get_root_path('musiquepy.website'), 'config.py')
        app.config.from_pyfile('config.py', silent=False)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():

        # Plugins init
        _init_session(app)
        _init_assets(app)

        # Blueprints
        from musiquepy.website.routes import auth, home, accounts, catalog

        app.register_blueprint(auth.bp)
        app.register_blueprint(home.bp)
        app.register_blueprint(accounts.bp)
        app.register_blueprint(catalog.bp)

        return app


def _init_session(app: Flask):
    sess.init_app(app)


def _init_assets(app: Flask):
    assets.init_app(app)

    assets.auto_build = True
    assets.debug = False

    style_bundle = Bundle(
        'src/*.scss',
        filters="scss,cssmin",
        output="dist/site.min.css", extra={'rel': 'stylesheet'})

    js_bundle = Bundle(
        'src/*.js',
        filters='jsmin',
        output='dist/site.min.js'
    )

    assets.register('app_styles', style_bundle)
    assets.register('app_scripts', js_bundle)
 
    if app.config['FLASK_ENV'] == 'development':
        style_bundle.build()
        js_bundle.build()


def _config_logging():
    dictConfig(
        {
            'version': 1,
            'formatters': {'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            }},
            'handlers': {'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'default'
            }},
            'root': {
                'level': 'DEBUG',
                'handlers': ['wsgi']
            }
        })
