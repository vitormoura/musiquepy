from flasgger import swag_from
from flask import Blueprint
from flask.json import jsonify
from musiquepy.data import get_musiquepy_db

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.get('/')
@swag_from('specs/get_users.yml')
def get_users():
    with get_musiquepy_db() as db:
        users = db.get_users()

        return jsonify([usr.to_dict() for usr in users])
