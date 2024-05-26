# to run: flask --app main --debug run

from flask import Flask, render_template, request
import requests
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/receive_data", methods=["POST"])
def receive_data():
    print(request.form["username"])
    return render_template("login.html", username=request.form["username"], password=request.form["password"])
    
if __name__ == "__main__":
    app.run(debug=True)