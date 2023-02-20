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
from models import db, User
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
    all_users = User.query.all()
    all_users = list(map(lambda user: user.serialize() ,all_users))
    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(all_users), 200

@app.route('/character', methods=['GET'])
def character():

    response_body = {
        "msg": "Hello, this is your GET /character response "
    }

    return jsonify(response_body), 200

@app.route('/character/<int:id>', methods=['GET'])
def get_one_character(id):

    response_body = {
        "msg": "Hello, this is your GET /character id response" +str(id)
    }

    return jsonify(response_body), 200

@app.route('/favorite/character/<int:character_id>',methods=['POST'])
def modify_favorite_character(character_id):
 
    return jsonify({"msg":"aqui se agrega el favorito " +str(character_id)+ "del personaje"}), 200

@app.route('/favorite/character/<int:character_id>',methods=['DELETE'])
def delete_favorite_character(character_id):

    return jsonify({"msg":"aqui se elimina el favorito " +str(character_id)+ "del personaje"}), 200
  

@app.route('/planet', methods=['GET'])
def planet():

    response_body = {
        "msg": "Hello, this is your GET /planet response"
    }

    return jsonify(response_body), 200

@app.route('/planet/<int:id>', methods=['GET'])
def get_one_planet(id):

    response_body = {
        "msg": "Hello, this is your GET /aqui esta el planeta con el id " +str(id)
    }

    return jsonify(response_body), 200

@app.route('/favorite/planet/<int:planet_id>',methods=['POST'])
def modify_favorite_planet(planet_id):

    return jsonify({"msg":"aqui se agrega el favorito " +str(planet_id)+ "del planeta"}), 200
   
@app.route('/favorite/planet/<int:planet_id>',methods=['DELETE'])
def delete_favorite_planet(planet_id):

    return jsonify({"msg":"aqui se elimina el favorito " +str(planet_id)+ "del planeta"}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
