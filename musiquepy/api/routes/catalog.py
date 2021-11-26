from flask import abort, Blueprint, request, session

from flask.json import jsonify

from musiquepy.api.utils import json_ok
from musiquepy.data import get_musiquepy_db
from musiquepy.data.schemas import GenericRecordSchema


bp = Blueprint('catalog', __name__, url_prefix='/catalog')

@bp.get('/genres')
def get_music_genres():
    with get_musiquepy_db() as db:
        genres = db.get_genres()
        schema = GenericRecordSchema(many=True)
        json_dump = schema.dumps(genres)

        return json_ok(json_dump)

@bp.get('/genres/<int:genre_id>')
def get_genre_by_id(genre_id:int):
    with get_musiquepy_db() as db:
        tracks = db.get_music_tracks_by_genre(genre_id)



        return jsonify(tracks)
