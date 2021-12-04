
from flask import Blueprint
from musiquepy.api.utils import json_ok
from musiquepy.data import get_musiquepy_db2

bp = Blueprint('catalog', __name__, url_prefix='/catalog')


@bp.get('/genres')
def get_music_genres():
    with get_musiquepy_db2() as db:
        genres = db.get_genres()

        return json_ok([g.to_dict(rules=('-artists',)) for g in genres])


@bp.get('/genres/<int:genre_id>')
def get_genre_by_id(genre_id: int):
    with get_musiquepy_db2() as db:
        tracks = db.get_music_tracks_by_genre(genre_id)

        return json_ok([t.to_dict() for t in tracks])
