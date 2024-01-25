# to run: flask --app main --debug run

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)

data_file = os.path.join(app.root_path, 'instance', 'new-books-collection.db')

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+data_file
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = ''

db = SQLAlchemy(app)
Bootstrap(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<Book {self.title}>'
    
    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating
        
with app.app_context():
    db.create_all()
    
    
class bookForm(FlaskForm):
    title = StringField(label='Book Name')
    author = StringField(label='Book Author')
    rating = StringField(label='Rating')
    submit = SubmitField('Submit')

class changeRatingForm(FlaskForm):
    new_rating = StringField(label='Rating')
    submit = SubmitField('Change Rating')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    form = changeRatingForm()
    book_to_edit = Book.query.get(id)
    if form.validate_on_submit():
        book_to_edit.rating = form.new_rating.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=book_to_edit, form=form)

@app.route('/delete/<id>')    
def delete(id):
    book_to_delete = Book.query.get(id)
    print(book_to_delete)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/')
def home():
    return render_template("index.html", books=Book.query.all())

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = bookForm()
    if form.validate_on_submit():
        new_book = Book(form.title.data, form.author.data, form.rating.data)
        db.session.add(new_book)
        db.session.commit()
       
        return redirect(url_for('home'))
    return render_template("add.html", form=form)

print("__name__", __name__)

if __name__ == "__main__":
    app.run(debug=True)

