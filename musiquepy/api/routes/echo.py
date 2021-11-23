from flask import abort, Blueprint, request, session

bp = Blueprint('echo', __name__, url_prefix='/echo')

@bp.get('/hello')
def get_message():
    return 'hello world'


