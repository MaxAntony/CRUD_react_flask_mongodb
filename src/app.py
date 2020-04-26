from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/pythonreactdb'

mongo = PyMongo(app)

db = mongo.db.users


@app.route('/users', methods=['GET'])
def get_userS():
    users = []
    for doc in db.find():
        users.append({
            '_id': str(ObjectId(doc['_id'])),
            'name': doc['name'],
            'email': doc['email'],
            'password': doc['password']
        })
    return jsonify(users)


@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    print(id)
    user = db.find_one({'_id': ObjectId(id)})
    print(user)
    return jsonify(user)


@app.route('/users', methods=['POST'])
def create_user():
    print(request.json)
    result = db.insert_one({
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password'],
    })
    return jsonify(str(result.inserted_id))


@app.route('/users/<id>', methods=['PUT'])
def update_user():
    return 'received'


@app.route('/users/<id>', methods=['DELETE'])
def delete_user():
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
