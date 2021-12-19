from flasgger import swag_from
from flask import abort, Blueprint
from flask.helpers import make_response
from musiquepy.data import get_musiquepy_db

bp = Blueprint('albums', __name__, url_prefix='/albums')


@bp.get('/<int:id>/photo')
@swag_from('specs/get_album_photo.yml')
def get_album_photo(id: int):
    if id <= 0:
        abort(400, 'invalid album id')

    with get_musiquepy_db() as db:
        photo = db.get_album_photo(id)

        if photo is None:
            abort(404)

        resp = make_response(photo.content, 200)
        resp.content_type = photo.content_type

        return resp
