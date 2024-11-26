"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Vehicle
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/characters', methods=['GET'])
def get_all_characters():

    characters = Character.query.all()
    if len(characters) <= 0:
        return jsonify({"error": "characters not found"}), 404
    response_body = [character.serialize() for character in characters]
    return jsonify(response_body), 200

@app.route('/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):

    character = Character.query.get_or_404(character_id)
    return jsonify(character.serialize()), 200

@app.route('/planets', methods=['GET'])
def get_all_planets():

    planets = Planet.query.all()
    if len(planets) <= 0:
        return jsonify({"error": "planets not found"}), 404
    response_body = [planet.serialize() for planet in planets]
    return jsonify(response_body), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):

    planet = Planet.query.get_or_404(planet_id)
    return jsonify(planet.serialize()), 200


@app.route('/vehicles', methods=['GET'])
def get_all_vehicles():

    vehicles = Vehicle.query.all()
    if len(vehicles) <= 0:
        return jsonify({"error": "vehicles not found"}), 404
    response_body = [vehicle.serialize() for vehicle in vehicles]
    return jsonify(response_body), 200

@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):

    vehicle = Vehicle.query.get_or_404(vehicle_id)
    return jsonify(vehicle.serialize()), 200


@app.route('/user/favorites', methods=['GET'])
def get_user_favorites():
    # Suponiendo que el usuario actual tiene id=1
    user = User.query.get(1)
    if len(user.favorites) <= 0:
        return jsonify({"error": "favorites not found"}), 404
    response_body = [favorite.serialize() for favorite in user.favorites]
    return jsonify(response_body), 200


# @app.route('/favorites/characters', methods=['POST'])
# def add_favorite_character():
#     # Suponiendo que el usuario actual tiene id=1
#     user = User.query.get(1)
#     if len(favorite.character) <= 0:
#         return jsonify({"error": "favorites not found"}), 404
#     response_body = [favorite.serialize() for favorite in user.favorites]
#     return jsonify(response_body), 200

# @app.route('/favorites/planets', methods=['POST'])
# def add_favorite_planet():
#     # Suponiendo que el usuario actual tiene id=1
#     user = User.query.get(1)
#     if len(favorites) <= 0:
#         return jsonify({"error": "favorites not found"}), 404
#     response_body = [favorite.serialize() for favorite in user.favorites]
#     return jsonify(response_body), 200

# @app.route('/favorites/vehicles', methods=['POST'])
# def add_favorite_vehicle():
#     # Suponiendo que el usuario actual tiene id=1
#     user = User.query.get(1)
#     if len(favorites) <= 0:
#         return jsonify({"error": "favorites not found"}), 404
#     response_body = [favorite.serialize() for favorite in user.favorites]
    # return jsonify(response_body), 200

@app.route('/favorites/characters/<int:character_id>', methods=['DELETE'])
def delete_favorite_character(character_id):
    favorite = Favorite.query.filter_by(user_id=1, character_id=character_id).first_or_404()
    db.session.delete(favorite)
    db.session.commit()
    return '', 204
    

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
