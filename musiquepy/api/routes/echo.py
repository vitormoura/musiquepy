from datetime import datetime
from flask import abort, Blueprint, request, session
from flask.json import jsonify

bp = Blueprint('echo', __name__, url_prefix='/echo')


@bp.get('/hello')
def get_message():
    # response text/html
    return 'hello world'


@bp.post('/content')
def post_echo_content():
    # response application/json (from dict -> to dict)

    content = request.get_json(silent=True)

    if content is None:
        return abort(400, 'json request body not informed')

    return jsonify(content)


@bp.post('/session/value-set')
def post_session_value_set():
    session['my_secret_value'] = str(datetime.now())
    return session['my_secret_value']


@bp.get('/session/value-get')
def get_session_value_get():
    if 'my_secret_value' in session:
        return session['my_secret_value']

    return '(empty)'
