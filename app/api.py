from flask import Blueprint, jsonify, request, make_response
from app.models import surveys_collection, users_collection
from datetime import datetime, timezone
from flask_jwt_extended import create_access_token
from app.queries import get_top_surveys_by_participants, get_votes_by_birth_year, get_average_choices

api = Blueprint('api', __name__)


# Récupérer les surveys
@api.route('/api/surveys', methods=['GET'])
def get_surveys():
    surveys = list(surveys_collection.find())
    for survey in surveys:
        survey['_id'] = str(survey['_id'])
    return jsonify(surveys), 200


# Créer un survey
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


# Créer un utilisateur
@api.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    required_fields = ['pseudo', 'password', 'password_confirm', 'date_of_birth', 'addresse', 'job']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    # Vérifier si l'utilisateur existe déjà
    if users_collection.find_one({'pseudo': data['pseudo']}):
        return jsonify({'error': 'pseudo already exists'}), 409

    # Ajouter l'utilisateur à la base de données
    user = {
        'pseudo': data['pseudo'],
        'password': data['password'],  # Stockage en clair
        'date_of_birth': data['date_of_birth'],
        'addresse': data['addresse'],
        'job': data['job'],
        'admin': data.get('admin', False)
    }

    result = users_collection.insert_one(user)
    return jsonify({'id': str(result.inserted_id)}), 201


@api.route('/api/login', methods=['POST'])
def login():
    try:
        # Récupérer les données JSON
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON format'}), 400

        # Vérifier les champs requis
        required_fields = ['pseudo', 'password']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        # Vérifier les informations de l'utilisateur
        user = users_collection.find_one({'pseudo': data['pseudo']})
        if not user or user['password'] != data['password']:
            return jsonify({'error': 'Invalid pseudo or password'}), 401

        # Préparer les données utilisateur (sans le mot de passe)
        user_data = {
            'pseudo': user['pseudo'],
            'age': user.get('age'),
            'address': user.get('address'),
            'job': user.get('job'),
            'admin': user.get('admin', False),
        }

        # Créer un token JWT
        access_token = create_access_token(identity=str(user['_id']), additional_claims=user_data)

        # Retourner la réponse
        response = {
            'message': 'Success',
            'token': access_token,
            'user': user_data
        }
        return jsonify(response), 200

    except Exception as e:
        print(f"Erreur lors du traitement de la requête: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

################################
# UC 10/11 - Dashboard Admin
################################

@api.route('/api/surveys/top', methods=['GET'])
def top_surveys():
    try:
        data = get_top_surveys_by_participants()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api.route('/api/surveys/<survey_id>/votes-by-birth-year', methods=['GET'])
def votes_by_year(survey_id):
    try:
        data = get_votes_by_birth_year(survey_id)
        if isinstance(data, dict):
            print(f"Données renvoyées pour le scrutin {survey_id}: {data}")
            return jsonify(data), 200
        else:
            return jsonify({"error": "Les données sont mal formatées."}), 500
    except Exception as e:
        print(f"Erreur dans la récupération des votes par année de naissance pour {survey_id}: {str(e)}")
        return jsonify({"error": str(e)}), 500


@api.route('/api/surveys/average_choices', methods=['GET'])
def average_choices():
    try:
        data = get_average_choices()
        return jsonify({"average_choices": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500