
from flask import Blueprint, render_template, request, session, abort
from flask.helpers import url_for
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash

from app.data import get_musiquepy_db
from ..errors import MusiquepyExistingUserError
from ..models.form_signup import FormSignup
from ..models.form_login import FormLogin

bp = Blueprint('accounts', __name__, url_prefix='/accounts')


@bp.get("/login")
def get_page_login():
    form = FormLogin()
    return render_template('accounts/login.html', form=form, submitted=False)


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
