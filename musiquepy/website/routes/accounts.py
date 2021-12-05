
from flask import (Blueprint, abort, current_app, g, render_template, request,
                   send_file, session)
from flask.helpers import url_for
from musiquepy.data import get_musiquepy_db
from musiquepy.data.errors import MusiquepyExistingUserError
from musiquepy.website.forms import FormSignup
from musiquepy.website.routes.auth import login_required
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

bp = Blueprint('accounts', __name__, url_prefix='/accounts')


@bp.get("/signup")
def page_signup():
    form = FormSignup()
    submitted = False

    if 'form_data' in session:

        submitted = True
        form_data = session.pop('form_data')
        form.process(ImmutableMultiDict(form_data))
        form.validate()

    return render_template('accounts/signup.html', form=form, submitted=submitted)


@bp.post("/signup")
def page_signup_post():

    form = FormSignup(request.form)
    usr = None

    if not form.validate():
        current_app.logger.info(
            'invalid form inputs, redirecting back to signup form')

        session['form_data'] = request.form.to_dict()
        return redirect(url_for('accounts.page_signup'))

    try:
        with get_musiquepy_db() as db:
            hashedPassword = generate_password_hash(form.user_password.data)
            usr = db.create_user(form.user_nickname.data,
                                 form.user_email.data, hashedPassword)
    except MusiquepyExistingUserError as err:
        abort(400, str(err))

    if usr is not None:
        return redirect(url_for('home.page_my_music'))

    return redirect(url_for('accounts.page_signup'))


@bp.get('/user-profile.jpg')
@login_required
def file_user_profile_picture():
    with get_musiquepy_db() as db:
        user_picture = db.get_user_profile_picture(g.user_id)
        return send_file(user_picture, mimetype="image/jpeg")


@bp.get('/user-profile')
@login_required
def page_user_profile():
    with get_musiquepy_db() as db:
        user = db.get_user_by_id(g.user_id)

        if user is None:
            abort(404)

        return render_template('accounts/profile.html', user=user)
