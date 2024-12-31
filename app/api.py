from flask import Blueprint, jsonify, request, make_response
from app.models import surveys_collection, users_collection
from datetime import datetime, timezone
from flask_jwt_extended import create_access_token
from "./static/algo/condorcy.py" import Condorcy
from "./static/algo/majority.py" import Majority
from "./static/algo/quantity_sort.py" import Quantity_Sort


api = Blueprint('api', __name__)


# Récupérer les surveys
@api.route('/api/surveys', methods=['GET'])
def get_surveys():
    surveys = list(surveys_collection.find())
    for survey in surveys:
        survey['_id'] = str(survey['_id'])
    return jsonify(surveys), 200

# Récupérer les 10 surveys les plus recement ferme
@api.route('/api/recentEndedSurveys', methods=['GET'])
def get_recentEndedSurveys():
    current_date = datetime.now().strftime('%Y-%m-%d')
    surveys = list(surveys_collection.find({
        'date.end': {'$lte': current_date}
    }).sort('date.create', -1).limit(10))
    
    for survey in surveys:
        survey['_id'] = str(survey['_id'])
    
    return jsonify(surveys), 200


# Récupérer les 10 surveys les plus recement update
@api.route('/api/recentUpdateSurveys', methods=['GET'])
def get_recentUpdatedSurveys():
    current_date = datetime.now().strftime('%Y-%m-%d')
    surveys = list(surveys_collection.find({
        'date.update': {'$lte': current_date}
    }).sort('date.create', -1).limit(10))
    
    for survey in surveys:
        survey['_id'] = str(survey['_id'])
    
    return jsonify(surveys), 200


# Affiche les details d'un survey
@api.route('/api/showSurvey', methods=['POST'])
def showSurvey():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Invalid JSON format'}), 400
    
    survey = surveys_collection.findOne({
        { "id" : data["id"] },
        'id':1, 'description': 1, 'question': 1, 'results': 1
    });
    
    return jsonify(surveys), 200



# Créer un survey
@api.route('/api/createSurveys', methods=['POST'])
def create_survey():
    data = request.get_json()
    required_fields = ['creator_id', 'question', 'choices', 'start_date', 'end_date', 'algo']
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
        'responses': [],
        'results': [],
        'algo': data['algo']
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


# Calcule le resultat d'un survey
@api.route('/api/calculateSurvey', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Invalid JSON format'}), 400
    
    survey = surveys_collection.find_one({"id": data["id"]})
    
    if survey['date']['end'] >= datetime.now().strftime('%Y-%m-%d') :
        
        modifications = {
            "$set" : {
                "result" : None
                }
        }
        
        match survey['algo'] :
            case 'condorcy' :
                modifications['$set']["result"] = Condorcy(survey['responses'])
            
            case 'majority':
                modifications['$set']["result"] = Majority(survey['responses'])
            
            case 'quantitySort':
                modifications['$set']["result"] = Quantity_Sort(survey['responses'])

        result = surveys_collectionresult = collection.update_one(
            {"id": data["id"]},
            modifications 
        )
        
        return jsonify({'result': str(result)}), 201

    else : 
        return jsonify({'result': None, 'message': "Cannot unfold now since the end date has not been passed"}), 201
    
    
    
# Calcule le resultat d'un survey
@api.route('/api/vote', methods=['POST'])
def vote():
    data = request.get_json() # data = {"id": id du survey, "data": {"response": input de l'user , "user_id': id de l'user}}
    
    if not data:
        return jsonify({'error': 'Invalid JSON format'}), 400
    
    survey = surveys_collection.find_one({"id": data["id"]})
    
    now = datetime.now().strftime('%Y-%m-%d')
    
    if survey['date']['end'] < now and survey['date']['start'] >= now :
        
        
        for response in survey['reponses'] :
            if response["user_id"] = data['data']['user_id'] :
                return jsonify({'result': None, "message" : "user already participated"}), 201
        
        
        modifications = {
            "$push" : {
                "reponses" : data['data']
                }
        }
        
        return jsonify({'result': "data send successfully"}), 201

    else : 
        return jsonify({'result': None, 'message': "Cannot unfold now since the end date has been passed or the starting date hasn't started"}), 201



@api.route('/api/modify', methods=['POST'])
def modify():
    data = request.get_json() # data = {"id": id du survey, "data": {"response": input de l'user {"description": str, "question": str, "choix": list} , "user_id': id de l'user}}
    
    if not data:
        return jsonify({'error': 'Invalid JSON format'}), 400
    
    survey = surveys_collection.find_one({"id": data["id"]})
    
    now = datetime.now().strftime('%Y-%m-%d')
    
    if survey['date']['end'] < now and survey['date']['start'] < now :
        if response["creator"]["user_id"]["$oid"] = data['data']['user_id'] :
            return jsonify({'result': None, "message" : "user isn't the creator of the survey"}), 201
        
        data_to_modify = {k: v for k, v in data['data']['response'].items() if v is not None}
            
        modifications = {
            "$set" : data_to_modify
        }
        
        return jsonify({'result': "modification done successfully"}), 201

    else : 
        return jsonify({'result': None, 'message': "Cannot modify since the end date has been passed or the starting date has started"}), 201



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
