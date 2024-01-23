# to run: flask --app main --debug run

from flask import Flask, render_template, request
import requests

posts = requests.get("https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json").json()

app = Flask(__name__)

def send_email(email):
    print(f"Name: {email['name']}\nemail: {email['email']}\nPhone: {email['phone']}\nMessage: {email['message']}")

@app.route("/")
@app.route("/index")
def home(posts=posts):
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

# ****** day 60  *******
@app.route("/contact", methods=["POST", "GET"])
def contact():
    method = request.method
    if method == "POST":
        send_email({'name': request.form['name'],
                    'email': request.form['email'],
                    'phone': request.form['phone'],
                    'message': request.form['message']})
    return render_template("contact.html", post=(method =="POST"))
        
    
    
@app.route("/post/<id>")
def post(id):
    for post in posts:
        print(type(post['id']))
        if post['id'] == int(id):
            return render_template("post.html", post=post)
    
if __name__ == "__main__":
    app.run(debug=True)