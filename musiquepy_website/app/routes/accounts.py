from flask import Blueprint, render_template, request
from ..models.form_signup import FormSignup

bp = Blueprint('accounts', __name__, url_prefix='/accounts')

@bp.route("/signup", methods=('post', 'get'))
def page_signup():
    form = FormSignup(request.form)

    if request.method == 'POST':
        form.validate()

        # TODO: Enregistrer nouvel utilisateur
    
    return render_template('signup.html', form=form, submitted=request.method == 'POST')
