
from flask import Blueprint, abort

from musiquepy.api.utils import json_ok
from musiquepy.data import get_musiquepy_db
from musiquepy.data.schemas import ArtistSchema

bp = Blueprint('artist', __name__, url_prefix='/artists')


@bp.get('/<int:artist_id>')
def get_artist_by_id(artist_id: int):
    with get_musiquepy_db() as db:
        artist = db.get_artist_by_id(artist_id)

        if artist is None:
            abort(404)

        schema = ArtistSchema()
        json_dump = schema.dumps(artist)

        return json_ok(json_dump)
