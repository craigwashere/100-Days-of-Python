# to run: flask --app server --debug run

from flask import Flask
import random

app = Flask(__name__)

magic_number = random.randrange(0,10)

@app.route("/")
def hello():
    return '<h2>Guess a number between 0 and 9</h2>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:input>")
def guess(input):
    if input < magic_number:
        return '<h2>Too low, try Again!</h2>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif input > magic_number:
        return '<h2>Too high, try Again!</h2>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h2>Correct!</h2>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'








if __name__ == "__main__":
    app.run(debug=True)