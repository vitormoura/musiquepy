from logging.config import dictConfig
import os

from flask import Flask

def create_app(test_config=None):

    # configure default logging
    _config_logging()

    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Blueprints
    from .routes import auth, home, accounts, catalog

    app.register_blueprint(auth.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(accounts.bp)
    app.register_blueprint(catalog.bp)

    return app


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
