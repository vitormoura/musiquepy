from flask import abort, Blueprint, render_template, request, session

bp = Blueprint('catalog', __name__, url_prefix='/catalog')


@bp.route('/home')
def get_catalog_home_page():
    return render_template('catalog/home.html')


@bp.route('/music/for-you')
def get_catalog_foryou_page():
    return render_template('catalog/for_you.html')


@bp.route('/music/<id>')
def get_catalog_musicdetail_page(id: str):
    id = id.strip()

    if len(id) == 0:
        return abort(404)

    return render_template('catalog/music_details.html', id=id)
