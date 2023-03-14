from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    employee_number = StringField(validators=[DataRequired()], label="Employee Number")
    password = PasswordField(validators=[DataRequired()], label="Password")
    submit = SubmitField(label="Login")
