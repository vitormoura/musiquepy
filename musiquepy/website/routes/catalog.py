from flask import abort, Blueprint, render_template

from musiquepy.website.model import MusicTracksViewModel
from musiquepy.data import get_musiquepy_db

bp = Blueprint('catalog', __name__, url_prefix='/catalog')


@bp.route('/home')
def page_home():
    with get_musiquepy_db() as db:
        return render_template('catalog/home.html', genres=db.get_genres())


@bp.route('/music/for-you')
def page_for_you():
    return render_template('catalog/for_you.html')


@bp.route('/music/<id>')
def page_music_detail(id: str):
    id = id.strip()

    if len(id) == 0:
        return abort(404)

    return render_template('catalog/music_details.html', id=id)


@bp.route('/genre/<int:id>')
def page_music_by_genre(id: int):
    with get_musiquepy_db() as db:
        genre = db.get_genre_by_id(id)

        if genre is None:
            abort(404)

        tracks = db.get_music_tracks_by_genre(genre.id)

        return render_template(
            'catalog/music_by_genre.html',
            id=id, genre=genre, tracks=MusicTracksViewModel(tracks)
        )
