from flask import abort, make_response
from app.models.form_login import FormLogin

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.post("/validate")
def post_validate_user_password():
    form = FormLogin(request.form)
    error = None

    if not form.validate():
        error = str(form.errors)

    if not check_password_hash('##hashed_password##', form.password):
        error = "utilisateur ou mot de passe invalides"

    if error is not None:
        return make_response(error, 400)

    return make_response('ok')
