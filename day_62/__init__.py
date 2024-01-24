# to run: flask --app main --debug run
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, URL
import csv
import os

app = Flask(__name__)

data_file = os.path.join(app.root_path, 'cafe-data.csv')

app.config['SECRET_KEY'] = ''
Bootstrap(app)

HIGHEST_RATING = 6

class CafeForm(FlaskForm):
    cafe_name = StringField(label='Cafe name', 
        validators=[
            DataRequired(message="This field is required.")
        ]
    )
    google_maps_url = StringField(label='Cafe Location on Google Maps (URL)', 
        validators=[
            URL(message='This is not a valid link'), 
            DataRequired(message="This field is required.")
        ]
    )
    open_time = StringField(label='Opening Time e.g. 8AM', 
        validators=[
            DataRequired(message="This field is required.")
        ]
    )
    close_time = StringField(label='Closing Time e.g. 5:30PM', 
        validators=[
            DataRequired(message="This field is required.")
        ]
    )
    coffee_rating = SelectField(
        label='Coffee Rating',
        choices=[(str(n), '☕️'*n or '✘') for n in range(1,HIGHEST_RATING)], 
        validators = [
            DataRequired(message="This field is required.")
        ]
    )
    wifi_strength = SelectField(
        label='Wifi Strength Rating',
        choices=[(str(n), '💪️'*n or '✘') for n in range(HIGHEST_RATING)], 
        validators=[
            DataRequired(message="This field is required.")
        ]
    )
    power_sockets = SelectField(
        label='Power Socket Availability',
        choices=[(str(n), '🔌️'*n or '✘') for n in range(HIGHEST_RATING)], 
        validators=[
            DataRequired(message="This field is required.")
        ]
    )
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
        with open(data_file, 'a', newline='', encoding="utf8") as csv_file:
            spamwriter = csv.writer(csv_file, delimiter=',')
            spamwriter.writerow([
                form.cafe_name.data,
                form.google_maps_url.data,
                form.open_time.data,
                form.close_time.data,
                int(form.coffee_rating.data)*'☕️' or '✘',
                int(form.wifi_strength.data)*'💪️' or '✘',
                int(form.power_sockets.data)*'🔌️' or '✘'
            ])
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes', methods=['GET', 'POST'])
def cafes():
    print("craig was here")
    with open(data_file, newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

@app.route("/")
def home():
    return render_template("index.html")

print("__name__", __name__)

if __name__ == '__main__':
    print("main")
    app.run(debug=True)
