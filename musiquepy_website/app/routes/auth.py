import functools

from flask import (
    Blueprint, g, request, session, render_template, redirect, url_for, abort, make_response
)
from werkzeug.security import check_password_hash
from app.forms import FormLogin
from app.db import get_musiquepy_db


SESSION_AUTH_USER_AUTHENTICATED = 'auth:user_authenticated'
SESSION_AUTH_USER_ID = 'auth:user_id'

bp = Blueprint('auth', __name__, url_prefix='/auth')

# Global


@bp.before_app_request
def load_current_user():
    g.user_id = session.get(SESSION_AUTH_USER_ID)

# Routes


@bp.get("/login")
def page_login():
    form = FormLogin()
    return render_template('auth/login.html', form=form, submitted=False)


@bp.post("/validate")
def post_validate_user_password():
    form = FormLogin(request.form)
    user = None

    if not form.validate():
        return abort(400, str(form.errors))

    with get_musiquepy_db() as db:
        user = db.get_user_by_email(form.username.data)

        if user is None:
            return abort(401)

    if not check_password_hash(user.password, form.password.data):
        return abort(401)

    session[SESSION_AUTH_USER_AUTHENTICATED] = True
    session[SESSION_AUTH_USER_ID] = user.id

    return make_response('ok')


@bp.post('/logout')
def post_logout():
    session.clear()

    return make_response('ok')

# Decorators


def login_required(view):

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        print('wrapped_view')
        if g.user_id is None:
            return redirect(url_for('auth.page_login'))

        return view(**kwargs)

    return wrapped_view
