# to run: flask --app server --debug run

from flask import Flask, render_template
from datetime import date
import requests

agify_URL = "https://api.agify.io"
genderize_URL = "https://api.genderize.io"

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html", year=date.today().year)

@app.route("/guess/<name>")
def guess(name=None):
    age = '0'
    gender = 'undefined'
    if name != None:
        params = {'name': name}
        age_response = requests.get(agify_URL, params).json()['age']
        gender_response = requests.get(genderize_URL, params).json()['gender']
    return render_template("guess.html", name=name.title(), 
            age=age_response, gender=gender_response, year=date.today().year)

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url).json()
    return render_template("blog.html", posts=blog_response)



if __name__ == "__main__":
    app.run(debug=True)