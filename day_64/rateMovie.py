from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class RateMovieForm(FlaskForm):
    rating = StringField(label='Your Rating out of 10')
    review = StringField(label='Your Review')
    submit = SubmitField('Done')
    