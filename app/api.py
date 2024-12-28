from flask import Blueprint, jsonify, request, make_response
from app.models import surveys_collection, users_collection
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

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
    required_fields = ['pseudo', 'password', 'age', 'addresse', 'job']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    # on verrif si l'user existe
    if users_collection.find_one({'pseudo': data['pseudo']}):
        return jsonify({'error': 'pseudo already exists'}), 409

    # on l'ajoute a la bdd
    user = {
        'pseudo': data['pseudo'],
        'password': generate_password_hash(data['password']),
        'age': data.get('age'),
        'addresse': data.get('addresse'),
        'job': data.get('job'),
        'admin': data.get('admin', False)
    }

    result = users_collection.insert_one(user)
    return jsonify({'id': str(result.inserted_id)}), 201

# Login Users
@api.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    required_fields = ['pseudo', 'password']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    # verif users par nom
    user = users_collection.find_one({'pseudo': data['pseudo']})
    if not user or not check_password_hash(user['password'], data['password']):
        return jsonify({'error': 'Invalid pseudo or password'}), 401
    
    # On retourne le token et les infos de l'utilisateur (sans le mot de passe)
    user_data = {
        'pseudo': user['pseudo'],
        'age': user['age'],
        'addresse': user['addresse'],
        'job': user['job'],
        'admin': user['admin']
    }

    # Création du token JWT
    access_token = create_access_token(
        identity=str(user['_id']),
        additional_claims=user_data
    )
    
    return jsonify({
        'token': access_token,
        'user': user_data
    }), 200