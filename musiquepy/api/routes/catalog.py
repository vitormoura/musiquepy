import json
from flask import Blueprint

from musiquepy.api.utils import json_ok
from musiquepy.data import get_musiquepy_db, get_musiquepy_db2
from musiquepy.data.schemas import GenericRecordSchema, MusicTrackSchema


bp = Blueprint('catalog', __name__, url_prefix='/catalog')


@bp.get('/genres')
def get_music_genres():
    db = get_musiquepy_db2()
    genres = db.get_genres()

    return json_ok([g.to_dict() for g in genres])


@bp.get('/genres/<int:genre_id>')
def get_genre_by_id(genre_id: int):
    with get_musiquepy_db() as db:
        tracks = db.get_music_tracks_by_genre(genre_id)
        schema = MusicTrackSchema(many=True)
        json_dump = schema.dumps(tracks)

        return json_ok(json_dump)
