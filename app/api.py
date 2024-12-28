from flask import Blueprint, jsonify, request, make_response
from app.models import surveys_collection, users_collection
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash

api = Blueprint('api', __name__)

# recup surveys
@api.route('/api/surveys', methods=['GET'])
def get_surveys():
    surveys = list(surveys_collection.find())
    for survey in surveys:
        survey['_id'] = str(survey['_id'])
    return jsonify(surveys), 200

# create surveys
@api.route('/api/surveys', methods=['POST'])
def create_survey():
    data = request.get_json()
    required_fields = ['creator_id', 'question', 'choices', 'start_date', 'end_date']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    survey = {
        'creator_id': data['creator_id'],
        'question': data['question'],
        'description': data.get('description', ''),
        'choices': data['choices'],
        'start_date': data['start_date'],
        'end_date': data['end_date'],
        'created_at': datetime.now(timezone.utc),
        'responses': []
    }

    result = surveys_collection.insert_one(survey)
    return jsonify({'id': str(result.inserted_id)}), 201

# create user
@api.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    required_fields = ['username', 'email', 'password', 'first_name', 'last_name']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    # on verrif si l'user existe
    if users_collection.find_one({'username': data['username']}):
        return jsonify({'error': 'Username already exists'}), 409

    if users_collection.find_one({'email': data['email']}):
        return jsonify({'error': 'Email already exists'}), 409

    # on l'ajoute a la bdd
    user = {
        'username': data['username'],
        'email': data['email'],
        'password': generate_password_hash(data['password']),
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'age': data.get('age'),
        'address': data.get('address'),
        'job': data.get('job'),
        'created_at': datetime.now(timezone.utc)
    }

    result = users_collection.insert_one(user)
    return jsonify({'id': str(result.inserted_id)}), 201

# Login Users
@api.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    required_fields = ['username', 'password']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    # verif users par nom
    user = users_collection.find_one({'username': data['username']})
    if not user or not check_password_hash(user['password'], data['password']):
        return jsonify({'error': 'Invalid username or password'}), 401

    return jsonify({'message': f'Welcome {user["username"]}!'}), 200
