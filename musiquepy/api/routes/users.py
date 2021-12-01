import json
from flask import Blueprint
from flask.json import jsonify

from musiquepy.data import get_musiquepy_db2
from musiquepy.data.db2 import User

bp = Blueprint('users', __name__, url_prefix='/user')


@bp.get('/')
def get_users():
    db = get_musiquepy_db2()
    users = db.get_users()

    return jsonify([usr.to_dict() for usr in users])
