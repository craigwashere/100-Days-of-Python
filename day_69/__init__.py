from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, LoginManager, login_required, current_user, logout_user
from .forms import CreatePostForm, RegisterForm, LoginForm, AddCommentForm
from flask_gravatar import Gravatar
from .Models import User, BlogPost, db, Comment
import os

app = Flask(__name__)
data_file = os.path.join(app.root_path, 'instance', 'blog.db')

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", '')
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
# database location locally: "sqlite:///blog.db"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", 'sqlite:///'+data_file)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
db.init_app(app)

gravatar = Gravatar(app, size=100, rating='x', default='retro', force_default=False,
                    force_lower=False, use_ssl=False, base_url=None)
                    
##CONFIGURE TABLES
with app.app_context():
    db.create_all()

login_manager = LoginManager()    
login_manager.init_app(app)

def admin_only(func):
    def wrapper(*args, **kwargs):
        print("wrapper")
        print(current_user.get_id())
        if current_user.get_id() is None or current_user.id != 1:
            abort(403)
        
        print("calling func")
        return func(*args, **kwargs)
      # Renaming the function name:
    wrapper.__name__ = func.__name__
    return wrapper

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/register', methods=['GET','POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        if db.session.query(User).filter_by(email=form.email.data).count() > 0:
            flash('Email already in use')
            return redirect(url_for('login'))
            
        new_user = User(
            name = form.name.data,
            email = form.email.data,
            password = generate_password_hash(
                password=form.password.data, 
                method='pbkdf2:sha256',
                salt_length=8
            )
        )
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user)
        return redirect(url_for('get_all_posts'))
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if not form.validate_on_submit():
        return render_template("login.html", form=form)
    
    user = db.session.query(User).filter_by(email=form.email.data).first()
    if user and check_password_hash(user.password, form.password.data):
        user.authenticated = True
        login_user(user, remember=True)
        return redirect(url_for('get_all_posts'))
    flash("Email not found or bad password")    
    return render_template("login.html", form=form)

    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    current_user.authenticated = False
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=['GET','POST'])
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    form = AddCommentForm()
    if form.validate_on_submit():
        if current_user.get_id() is None:
            flash("Login Required")
            return redirect(url_for('login'))
            
        new_comment = Comment(
            text = form.body.data,
            comment_author = current_user,
            parent_post = requested_post
        )
        db.session.add(new_comment)
        db.session.commit()
        
    return render_template("post.html", post=requested_post, form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=['GET','POST'])
@admin_only
def add_new_post():
    print("add_new_post")
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
        
    print("add_new_post 2")
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=['GET','POST'])
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        # author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        # post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
