from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime

import os

app = Flask(__name__)

data_file = os.path.join(app.root_path, 'instance', 'posts.db')

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+data_file
app.config['SECRET_KEY'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ckeditor = CKEditor(app)
Bootstrap(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
    cancel = SubmitField(label='Cancel', render_kw={'formnovalidate': True})

@app.route("/delete_post/<int:index>")
def delete_post(index):
    requested_post = db.session.query(BlogPost).get(index)
    db.session.delete(requested_post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))
    
@app.route("/new-post", methods=['GET','POST'])
def new_post():
    form = CreatePostForm()
    if form.cancel.data:  # if cancel button is clicked, the form.cancel.data will be True
        return redirect(url_for('get_all_posts'))
    if form.validate_on_submit():
        new_post = BlogPost(
            title = form.title.data,
            subtitle = form.subtitle.data,
            date = datetime.datetime.now().strftime("%B %d, %Y"),
            body = form.body.data,
            author = form.author.data,
            img_url = form.img_url.data
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form = form)
    
@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = db.session.query(BlogPost).get(index)
    return render_template("post.html", post=requested_post)

@app.route("/edit_post/<int:post_id>", methods=['GET','POST'])
def edit_post(post_id):
    post = db.session.query(BlogPost).get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.cancel.data:  # if cancel button is clicked, the form.cancel.data will be True
        return redirect(url_for('get_all_posts'))
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=edit_form, post=post)
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)