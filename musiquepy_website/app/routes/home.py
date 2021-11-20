from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route("")
def home_index():
    return render_template('home.html')

@bp.route("my-music")
def page_my_music():
    return render_template('my_music.html')


