from logging import Logger
from logging.config import dictConfig
from flasgger import Swagger
import os

from flask import Flask
from flask_cors import CORS

swagger = Swagger()
cors = CORS()


def create_app(test_config=None, logger_override: Logger = None):

    # configure default logging
    _config_logging()

    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=False)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # logging
    if logger_override:
        app.logger.handlers = logger_override.handlers
        app.logger.setLevel(logger_override.level)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():

        # Plugins init
        cors.init_app(app)
        swagger.init_app(app)

        # Blueprints
        from musiquepy.api.routes import echo, catalog, artists, users

        app.register_blueprint(echo.bp)
        app.register_blueprint(catalog.bp)
        app.register_blueprint(artists.bp)
        app.register_blueprint(users.bp)

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
