# to run: flask --app main --debug run
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import requests
import json

app = Flask(__name__)
Bootstrap(app)
	
def get_XKCD_URL(id: int) -> str:
    if id is None:
        return "https://xkcd.com/info.0.json"
    else:
        return f"https://xkcd.com/{id}/info.0.json"
    
@app.route("/")
def home():
    try:
        id = request.args['id']
        if int(id) < 1:
            id = None
    except:
        id = None
        
    response = requests.get(get_XKCD_URL(id))

    if response.status_code == 404:
        id = '1'
        response = requests.get(get_XKCD_URL(id))
        
    return render_template("index.html", image=json.loads(json.dumps(response.json())))
    
if __name__ == '__main__':
    app.run(debug=True)