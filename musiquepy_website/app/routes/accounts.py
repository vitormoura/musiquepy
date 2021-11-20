
from flask import Blueprint, render_template, request, session, abort, current_app
from flask.helpers import url_for
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash

from app.db import get_musiquepy_db
from app.errors import MusiquepyExistingUserError
from app.forms import FormSignup

bp = Blueprint('accounts', __name__, url_prefix='/accounts')


@bp.get("/signup")
def get_page_signup():
    form = FormSignup()
    submitted = False

    if 'form_data' in session:

        submitted = True
        form_data = session.pop('form_data')
        form.process(ImmutableMultiDict(form_data))
        form.validate()

    return render_template('accounts/signup.html', form=form, submitted=submitted)


@bp.post("/signup")
def post_page_signup():

    form = FormSignup(request.form)
    usr = None

    if not form.validate():
        current_app.logger.info('invalid form inputs, redirecting back to signup form')

        session['form_data'] = request.form.to_dict()
        return redirect(url_for('accounts.get_page_signup'))

    try:
        with get_musiquepy_db() as db:
            hashedPassword = generate_password_hash(form.user_password.data)
            usr = db.create_user(form.user_nickname.data,
                                 form.user_email.data, hashedPassword)
    except MusiquepyExistingUserError as err:
        abort(400, str(err))

    if usr is not None:
        return redirect(url_for('home.page_my_music'))

    return redirect(url_for('accounts.get_page_signup'))
