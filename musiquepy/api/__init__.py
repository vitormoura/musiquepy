from logging.config import dictConfig
import os

from flask import Flask

def create_app(test_config=None):

    # configure default logging
    _config_logging()

    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)

    if test_config is None:
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
        from musiquepy.api.routes import echo

        # Blueprints
        app.register_blueprint(echo.bp)

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
