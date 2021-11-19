from app.models.form_login import FormLogin
from flask import Blueprint, render_template, request, session
from flask.helpers import make_response, url_for
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.utils import redirect
from ..models.form_signup import FormSignup
from werkzeug.security import generate_password_hash

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

    if not form.validate():
        session['form_data'] = request.form.to_dict()
        return redirect(url_for('accounts.get_page_signup'))

    hashedPassword = generate_password_hash(form.user_password)

    # TODO: Enregistrer nouvel utilisateur
    return make_response('signup ok')
