from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    """Login form."""
    email = StringField(
        label='Email',
        validators=[
        Email(message=('Not a valid email address')),
        DataRequired()
        ]
    )
    password = PasswordField(
        label='Password', 
        validators=[
            Length(min=8, message=('Password too short')),
            DataRequired()
        ]
    )
    
    submit = SubmitField(label='Log in')