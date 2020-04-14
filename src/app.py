from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/pythonreactdb'

mongo = PyMongo(app)

db = mongo.db.users


@app.route('/users', method=['GET'])
def get_userS():
    return 'received'


@app.route('/user/<id>', method=['GET'])
def get_user():
    return 'received'


@app.route('/users', method=['POST'])
def create_user():
    print(request.json())
    return 'received'


@app.route('/users/<id>', method=['PUT'])
def update_user():
    return 'received'


@app.route('/users/<id>', method=['DELETE'])
def delete _user():
    return 'received'


@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'message': 'resource not found '+request.url,
        'status': 404
    })
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(debug=True)
