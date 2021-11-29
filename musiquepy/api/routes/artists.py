from flask import Blueprint, abort, send_from_directory

from musiquepy.api.utils import json_ok
from musiquepy.data import get_musiquepy_db
from musiquepy.data.schemas import ArtistSchema

bp = Blueprint('artist', __name__, url_prefix='/artists')


@bp.get('/<int:artist_id>/info')
def get_artist_by_id(artist_id: int):
    with get_musiquepy_db() as db:
        artist = db.get_artist_by_id(artist_id)

        if artist is None:
            abort(404)

        schema = ArtistSchema()
        json_dump = schema.dumps(artist)

        return json_ok(json_dump)


@bp.get('/<int:artist_id>/image')
def get_artist_image(artist_id: int):
    return send_from_directory("static/images", f'mp_artist_{artist_id}.jpg')
