from app.data import get_musiquepy_db
from flask import abort, Blueprint, render_template, request, session

bp = Blueprint('catalog', __name__, url_prefix='/catalog')


@bp.route('/home')
def get_catalog_home_page():
    with get_musiquepy_db() as db:
        return render_template('catalog/home.html', genres=db.get_genres())


@bp.route('/music/for-you')
def get_catalog_foryou_page():
    return render_template('catalog/for_you.html')


@bp.route('/music/<id>')
def get_catalog_musicdetail_page(id: str):
    id = id.strip()

    if len(id) == 0:
        return abort(404)

    return render_template('catalog/music_details.html', id=id)


@bp.route('/genre/<int:id>')
def get_catalog_music_by_genre(id: int):
    with get_musiquepy_db() as db:
        genre = db.get_genre_by_id(id)

        if genre is None:
            abort(404)

        return render_template('catalog/music_by_genre.html', id=id, genre=genre)
