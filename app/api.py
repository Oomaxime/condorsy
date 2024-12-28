from flask import Blueprint, jsonify, request
from app.models import Survey, surveys_collection
from datetime import datetime, UTC

api = Blueprint('api', __name__)

@api.route('/api/surveys', methods=['GET'])
def get_surveys():
    surveys = list(surveys_collection.find())
    # Convertir ObjectId en str pour la sérialisation JSON
    for survey in surveys:
        survey['_id'] = str(survey['_id'])
    return jsonify(surveys)

@api.route('/api/surveys', methods=['POST'])
def create_survey():
    data = request.get_json()
    
    survey = {
        'creator_id': data.get('creator_id'),
        'question': data.get('question'),
        'description': data.get('description'),
        'choices': data.get('choices', []),
        'start_date': data.get('start_date'),
        'end_date': data.get('end_date'),
        'created_at': datetime.now(UTC),
        'responses': []
    }
    
    result = surveys_collection.insert_one(survey)
    return jsonify({'id': str(result.inserted_id)}), 201