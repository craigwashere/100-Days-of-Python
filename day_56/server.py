# to run: flask --app server --debug run

from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")







if __name__ == "__main__":
    app.run(debug=True)