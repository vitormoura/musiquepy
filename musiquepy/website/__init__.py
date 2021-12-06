import os
from datetime import datetime
from logging.config import dictConfig

from flask import Flask
from flask.templating import render_template
from flask_assets import Bundle, Environment
from flask_session import Session

from musiquepy.website.i18n import set_lang

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

        set_lang(app.config.get('APP_DEFAULT_LANG', 'en'))

        # Plugins init
        _init_session(app)
        _init_assets(app)

        # Blueprints
        from musiquepy.website.routes import accounts, auth, catalog, home

        app.register_blueprint(auth.bp)
        app.register_blueprint(home.bp)
        app.register_blueprint(accounts.bp)
        app.register_blueprint(catalog.bp)

        # Template filters
        _config_template_filters(app)

        # Global handlers
        _config_other_handlers(app)

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


def _config_other_handlers(app: Flask):

    @app.errorhandler(404)
    def page_error_not_found(err):
        return render_template('_not_found.html')


def _config_template_filters(app: Flask):
    @app.template_filter('tsdatetostr')
    def _jinja2_filter_timestamp_datetime(timestamp_date:float, fmt=None):
        dt = datetime.fromtimestamp(timestamp_date)
        return str(dt)
        
