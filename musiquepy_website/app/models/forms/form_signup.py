from wtforms import Form, validators
from wtforms.fields.simple import BooleanField, StringField


class FormSignup(Form):
    user_email = StringField("Quel est votre courriel?", validators=[
                             validators.InputRequired(), validators.Email()])
    user_email_confirm = StringField("Confirmez votre courriel", validators=[
                                     validators.InputRequired(), validators.Email(), validators.EqualTo('user_email')])
    user_password = StringField("Créez un mot de passe", validators=[validators.InputRequired(
    ), validators.Regexp('^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])[a-zA-Z0-9]{8,20}$')])
    user_nickname = StringField("Nous vous appelerons comment?", validators=[
                                validators.InputRequired()])
    user_marketing_ok = BooleanField("Partagez des données pour le marketing")
