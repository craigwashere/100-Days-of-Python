# to run: flask --app main --debug run
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import ValidationError, DataRequired, URL

import os

app = Flask(__name__)

data_file = os.path.join(app.root_path, 'instance', 'cafes.db')

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+data_file;
print(app.instance_path)
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db = SQLAlchemy(app)
Bootstrap(app)

HIGHEST_RATING = 6

class CafeForm(FlaskForm):
    name = StringField(label='Cafe name', 
        validators=[
            DataRequired(message="This field is required.")
        ]
    )
    map_url = StringField(label='Cafe Location on Google Maps (URL)', 
        validators=[
            URL(message='This is not a valid link'), 
            DataRequired(message="This field is required.")
        ]
    )
    img_url = StringField(label='URL for image', 
        validators=[
            DataRequired(message="This field is required.")
        ]
    )
    location = StringField(label='Location in London', 
        validators=[
            DataRequired(message="This field is required.")
        ]
    )
    has_sockets = BooleanField(label='Has Power Sockets?')
    has_toilet = BooleanField(label='Has Toilets?')
    has_wifi = BooleanField(label='Has WiFi?')
    can_take_calls = BooleanField(label='Can Take Calls?')
    seats = SelectField(
        label='Number of Seats',
        choices=["0-10", "10-20", "20-30", "30-40", "50+"], 
        validators = [
            DataRequired(message="This field is required.")
        ]
    )
    coffee_price = StringField(label='Average Price per Coffee', 
        validators=[
            DataRequired(message="This field is required.")
        ]
    )
    submit = SubmitField('Submit')
    cancel = SubmitField('Cancel')

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)
    
    # def __repr__(self):
        # return f'<Book {self.title}>'
    
    def __init__(self, name, map_url, img_url, location, has_sockets, 
                    has_toilet, has_wifi, can_take_calls, seats, coffee_price):
        self.name = name
        self.map_url = map_url
        self.img_url = img_url
        self.location = location
        self.has_sockets = has_sockets
        self.has_toilet = has_toilet
        self.has_wifi = has_wifi
        self.can_take_calls = can_take_calls
        self.seats = seats
        self.coffee_price = coffee_price
        
# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/delete/<id>')    
def delete(id):
    cafe_to_delete = Cafe.query.get(id)
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect(url_for('cafes'))

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    edit_form = CafeForm()
    cafe_to_edit = Cafe.query.get(id)
    if request.method == 'GET':
        edit_form.process(obj=cafe_to_edit)
    else: # request.method == 'POST':
        print("post")
        if edit_form.cancel.data:
            return redirect(url_for('cafes'))
        if edit_form.validate_on_submit():
            edit_form.populate_obj(cafe_to_edit)
            db.session.commit()
            return redirect(url_for('cafes'))
        
    return render_template("add.html", cafe=cafe_to_edit, form=edit_form)

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("true")
        new_cafe = Cafe(form.name.data, form.map_url.data,
                        form.img_url.data, form.location.data,
                        form.has_sockets.data, form.has_toilet.data,
                        form.has_wifi.data, form.can_take_calls.data, form.seats.data,
                        form.coffee_price.data)
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    cafes = []
    for u in Cafe.query.all():
        cafes.append({k:v for (k,v) in u.__dict__.items() if not k.startswith("_sa_")})
    
    return render_template('cafes.html', cafes=cafes)

print("__name__", __name__)

if __name__ == '__main__':
    print("main")
    app.run(debug=True)
