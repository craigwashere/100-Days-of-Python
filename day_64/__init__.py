from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

# prepend '.' for module deployment
from rateMovie import RateMovieForm
from addMovie import addMovieForm
from tmdb import TMDB
import os

app = Flask(__name__)

data_file = os.path.join(app.root_path, 'instance', 'new-books-collection.db')
print(app.instance_path)
##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+data_file;
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = ''
db = SQLAlchemy(app)
Bootstrap(app)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    release_year = db.Column(db.Integer)
    review = db.Column(db.String(250))
    overview = db.Column(db.String(250), nullable=False)
    bg_image = db.Column(db.String(250))
    rating = db.Column(db.Float)
    
    def __repr__(self):
        return f'<Book {self.title}>'
    
    def __init__(self, id, title, release_year, review, overview, bg_image, rating):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.review = review
        self.overview = overview
        self.bg_image = bg_image
        self.rating = rating

        
with app.app_context():
    db.create_all()

@app.route("/delete")
def delete():
    movie_to_delete = Movies.query.get(request.args.get('id'))
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = RateMovieForm()
    print("id", request.args.get('id'))
    if form.cancel.data:  # if cancel button is clicked, the form.cancel.data will be True
        return redirect(url_for('home'))
    movie_to_edit = Movies.query.get(request.args.get('id'))
    if form.validate_on_submit():
        movie_to_edit.rating = form.rating.data if form.rating.data != '' else 0.0
        movie_to_edit.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie_to_edit, form=form)

@app.route("/select")
def select():
    movie_id = request.args.get('id')
    print(movie_id)
    response = TMDB().find_movie(movie_id)
    print("year", response.get('release_date'))
    movie_to_add = Movies(
        id = movie_id,
        title=response.get('title'),
        release_year=response.get('release_date')[:4],
        overview = response.get('overview'),
        bg_image = f"https://image.tmdb.org/t/p/original{response.get('poster_path')}",
        review = "",
        rating = 0
    )
    db.session.add(movie_to_add)
    db.session.commit()
    return redirect(url_for('edit', id=movie_id))
    
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = addMovieForm()
    if form.cancel.data:  # if cancel button is clicked, the form.cancel.data will be True
        return redirect(url_for('home'))    
    if form.validate_on_submit():
        tmdb = TMDB()
        return render_template('select.html', movies=tmdb.search_movie(form.title.data))
    return render_template('add.html', form=form)
    
@app.route("/")
def home():
    movies=Movies.query.order_by(Movies.rating.desc()).all()
    return render_template("index.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
