from flask import abort, Blueprint, request
from flask.json import jsonify

bp = Blueprint('echo', __name__, url_prefix='/echo')

@bp.get('/hello')
def get_message():
    return 'hello world'


@bp.post('/content')
def post_echo_content():
    content = request.get_json(silent=True)

    if content is None:
        return abort(400, 'json request body not informed')

    return jsonify(content)
