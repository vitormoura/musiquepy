from musiquepy.website.routes.auth import login_required
from musiquepy.website.i18n import _
from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')


@bp.route("")
def page_index():
    return render_template('home.html', welcome_msg=_('welcome message'))


@bp.route("my-music")
@login_required
def page_my_music():
    return render_template('my_music.html')
