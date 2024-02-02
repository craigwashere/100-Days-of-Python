from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask import Response
import random
from sqlalchemy.orm.exc import NoResultFound
import os

app = Flask(__name__)

data_file = os.path.join(app.root_path, 'instance', 'cafes.db')

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+data_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    
    def __repr__(self):
        return f'<Book {self.title}>'

@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    cafe = random.choice(db.session.query(Cafe).all())
    print(cafe)
    return jsonify({column.name: cafe.__getattribute__(column.name) for column in Cafe.__table__.columns})
    
@app.route("/all")
def all():
    cafes = db.session.query(Cafe).all()
    return jsonify({'cafes': [{column.name: cafe.__getattribute__(column.name) for column in Cafe.__table__.columns} for cafe in cafes]})
    
@app.route("/search")
def search():
    print("loc", request.args.get('loc'))
    cafes = db.session.query(Cafe).filter(Cafe.location==request.args.get('loc'))
    print("cafes", cafes)
    if cafes.count() == 0:
        return jsonify({'error': {"Not Found": "Sorry, we don't have a cafe at that location."}})
    else:
        return jsonify({'cafes': [{column.name: cafe.__getattribute__(column.name) for column in Cafe.__table__.columns} for cafe in cafes]})

## HTTP POST - Create Record
def make_bool(val: int) -> bool:
    return bool(int(val))
    
@app.route("/add", methods=['POST'])
def add():
    try:
        new_cafe = Cafe(
            name=request.form['name'],
            map_url=request.form['map_url'],
            img_url=request.form['img_url'],
            location=request.form['location'], 
            seats=request.form['seats'], 
            has_toilet=make_bool(request.form.get('has_toilet')),
            has_wifi=make_bool(request.form['has_wifi']), 
            has_sockets=make_bool(request.form['has_sockets']), 
            can_take_calls=make_bool(request.form['can_take_calls']), 
            coffee_price=request.form['coffee_price']
        )
        print((new_cafe.has_toilet))
    except:
        return jsonify({'error': {"bad data": "incorrect or missing data"}})
    else:
        try: 
            db.session.add(new_cafe)
            db.session.commit()
        except:
            return jsonify({'error': {"database error": "database error"}})
        
    return jsonify({'response': {"success": "Successfully added new cafe"}})
## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args.get('new_price')
    print("new_price", new_price)
    cafe = db.session.query(Cafe).get(cafe_id)
    cafe.coffee_price = new_price
    try:
        db.session.commit()
    except:
        return jsonify({'error': {"Not Found": "Flask is being a piece of shit again."}})
    else:
        return jsonify({"Success": "Successfully updated price"})
      
## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=['DELETE'])
def report_closed(cafe_id):
    print(request.args.get('api-key'))
    api_key = request.args.get('api-key')
    if api_key != 'TopSecretAPIKey':
        return Response("{'error': 'Flask is being a piece of shit again.'}", status=403, mimetype='application/json')
        
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe is None:
        return Response("{'error': 'Can't find cafe.'}", status=404, mimetype='application/json')
    db.session.delete(cafe)
    db.session.commit()
    return jsonify({"Success": "Successfully deleted cafe"})
    

if __name__ == '__main__':
    app.run(debug=True)
