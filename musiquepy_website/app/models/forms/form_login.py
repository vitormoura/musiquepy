from wtforms import Form, validators
from wtforms.fields.simple import BooleanField, StringField


class FormLogin(Form):
    username = StringField("Nom d'utilisateur",
                           validators=[validators.InputRequired()])
    password = StringField(
        "Mot de passe", validators=[validators.InputRequired()])
