from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class addMovieForm(FlaskForm):
    title = StringField(label='Title')
    submit = SubmitField('Submit')
    cancel = SubmitField(label='Cancel', render_kw={'formnovalidate': True})
    