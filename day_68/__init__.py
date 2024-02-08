from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

import os

app = Flask(__name__)

data_file = os.path.join(app.root_path, 'instance', 'users.db')

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+data_file
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
db = SQLAlchemy(app)

login_manager.init_app(app)

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

    def is_active(self):
        return True;
        
    def get_id(self):
        return self.id
        
    def is_authenticated(self):
        return self.authenticated
        
    def is_anonymous(self):
        return False;


@app.route('/')
def home():
    return render_template("index.html", logged_in = current_user.is_authenticated )


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        form_name = request.form.get('name')
        form_email = request.form.get('email')
        if User.query.filter_by(email=form_email).count() > 0:
            flash("Email already in use")
            return render_template("register.html")
            
        new_user = User(
            name = request.form.get('name'),
            email = request.form.get('email'),
            password = generate_password_hash(
                password=request.form.get('password'), 
                method='pbkdf2:sha256',
                salt_length=8
            )
        )
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user)
        return redirect(url_for('secrets', name=form_name))
    else:
        return render_template("register.html")


@app.route('/login', methods=['GET','POST'])
def login():
    # form = LoginForm()
    if request.method == 'GET':
        return render_template("login.html")
        
    user = db.session.query(User).filter_by(email=request.form['email']).first()
    if user and check_password_hash(user.password, request.form['password']):
        user.authenticated = True
        login_user(user, remember=True)
        return redirect(url_for('secrets'))
    flash("Email not found or bad password")    
    return render_template("login.html")

    
@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name = current_user.name)


@app.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    print(url_for('static', filename='files'))
    return send_from_directory(directory='./static', path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
