from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    open_id = StringField("openid", validators=[DataRequired()])
    remember_me = BooleanField("remember_me", default=False)

