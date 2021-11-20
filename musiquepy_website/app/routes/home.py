from app.routes.auth import login_required
from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route("")
def home_index():
    return render_template('home.html')

@bp.route("my-music")
@login_required
def page_my_music():
    return render_template('my_music.html')


