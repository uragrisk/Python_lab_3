from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import mysql.connector
import json
import copy

print("hgngkjn")

with open('secret.json') as f:
    SECRET = json.load(f)

#DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
        # user=SECRET["user"],
        # password=SECRET["password"],
        # host=SECRET["host"],
        # port=SECRET["port"],
        # db=SECRET["db"])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:aa123456@localhost:3306/Lab6"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tonnage = db.Column(db.Float, primary_key=True)
    max_speed = db.Column(db.Integer, primary_key=True)
    fuel_per_100miles = db.Column(db.Float, primary_key=True)
    movement_surface = db.Column(db.String(32), unique=False)
    movement_type = db.Column(db.String(32), unique=False)

    def __init__(self, tonnage = 0, max_speed = 0, fuel_per_100miles = 0.0, movement_surface = "N/A" , movement_type = "N/A"):
        self.tonnage = tonnage
        self.max_speed = max_speed
        self.fuel_per_100miles = fuel_per_100miles
        self.movement_surface = movement_surface
        self.movement_type = movement_type

class ShipSchema(ma.Schema):
    class Meta:
        fields = ('tonnage', 'max_speed', 'fuel_per_100miles', 'movement_surface'\
            'movement_type', 'name')

ship_schema = ShipSchema()
ships_schema = ShipSchema(many = True)

@app.route("/ship", methods=["POST"])
def add_ship():
    ship = Ship(request.json['tonnage'],
                request.json['max_speed'],
                request.json['fuel_per_100miles'],
                request.json['movement_surface'],
                request.json['movement_type'])
    db.session.add(ship)
    db.session.commit()
    return ship_schema.jsonify(ship)

@app.route("/ship", methods=["GET"])
def get_ship():
    all_ship = Ship.query.all()
    result = ship_schema.dump(all_ship)
    return jsonify(result)

@app.route("/ship/<id>", methods=["GET"])
def ship_detail(id):
    ship = Ship.query.get(id)
    if not ship:
        abort(404)
    return ship_schema.jsonify(ship)

@app.route("/ship/<id>", methods=["PUT"])
def ship_update(id):
    ship = Ship.query.get(id)
    if not ship:
        abort(404)
    old_ship = copy.deepcopy(ship)
    ship.price = request.json['tonnage']
    ship.operating_voltage_in_watts = request.json['max_speed']
    ship.current_consumption_in_watts = request.json['fuel_per_100miles']
    ship.model_name = request.json['movement_surface']
    ship.manufacturer = request.json['movement_type']
    ship.commit()
    return ship_schema.jsonify(old_ship)

@app.route("/ship/<id>", methods=["DELETE"])
def ship_delete(id):
    ship = Ship.query.get(id)
    if not ship:
        abort(404)
    db.session.delete(ship)
    db.session.commit()
    return ship_schema.jsonify(ship)

if __name__ == '__main__':

    app.run(debug=True, host='127.0.0.1')


