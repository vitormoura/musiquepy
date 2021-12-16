import logging

from musiquepy.api import create_app
from werkzeug.middleware.proxy_fix import ProxyFix

gunicorn_logger = logging.getLogger('gunicorn.error')

app = create_app(logger_override=gunicorn_logger)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)
