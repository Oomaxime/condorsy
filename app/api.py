from flask import Blueprint, jsonify, request, make_response
from app.models import surveys_collection, users_collection
from datetime import datetime, timezone
from flask_jwt_extended import create_access_token
from app.queries import get_top_surveys_by_participants, get_votes_by_birth_year, get_average_choices
from bson.objectid import ObjectId
import sys
import os

# Ajout le dossier "static/algo" au chemin d'importation
sys.path.append(os.path.join(os.path.dirname(__file__), 'static', 'algo'))

# Importer les algos comme des modules Python
from condorcy import Condorcy
from majority import Majority
from quantity_sort import Quantity_Sort


api = Blueprint('api', __name__)

#####################################################
# Récup tout les surveys
#####################################################
@api.route('/api/surveys', methods=['GET'])
def get_surveys():
    """
    Récupère tous les sondages dans la base de données.

    La fonction effectue une recherche dans la collection des sondages pour obtenir
    tous les sondages sans aucune condition de filtre. Elle convertit l'ObjectId de chaque
    sondage en chaîne de caractères pour les rendre facilement utilisables dans la réponse.

    Étapes de la fonction :
    - Récupère tous les sondages de la collection.
    - Convertit l'ObjectId de chaque sondage en chaîne de caractères.
    - Renvoie la liste des sondages.

    Retourne :
        - 200 : Liste de tous les sondages dans la base de données, avec leurs détails.
        - Chaque sondage contient les informations comme l'id, la question, la description, etc.

    Exemple de réponse :
    - Succès :
        [
            {
                "id": "<id_survey>",
                "description": "Description du sondage",
                "question": "Question posée",
                "date": {
                    "create": "2024-12-30",
                    "end": "2024-12-31"
                },
                ...
            },
            ...
        ]
    """
    surveys = list(surveys_collection.find())
    for survey in surveys:
        survey['_id'] = str(survey['_id'])
    return jsonify(surveys), 200


#####################################################
# Récup les 10 surveys les plus recent fermé
#####################################################
@api.route('/api/recentEndedSurveys', methods=['GET'])
def get_recentEndedSurveys():
    """
    Récupère les 10 sondages les plus récemment fermés, triés par date de création.

    La fonction effectue une recherche dans la collection des sondages pour obtenir
    les 10 sondages qui ont une date de fin antérieure ou égale à la date actuelle.
    Elle trie les résultats par date de création et renvoie les informations sous forme de liste.

    Étapes de la fonction :
    - Récupère la date actuelle.
    - Recherche les sondages dont la date de fin est inférieure ou égale à la date actuelle.
    - Trie les sondages par date de création, de la plus récente à la plus ancienne.
    - Limite la réponse aux 10 premiers sondages.
    - Convertit l'ObjectId en chaîne de caractères pour chaque sondage.

    Retourne :
        - 200 : Liste des 10 sondages les plus récents qui sont fermés, avec leurs détails.
        - Chaque sondage contient les informations comme l'id, la question, la description, la date de fin, etc.

    Exemple de réponse :
    - Succès :
        [
            {
                "id": "<id_survey>",
                "description": "Description du sondage",
                "question": "Question posée",
                "date": {
                    "create": "2024-12-30",
                    "end": "2024-12-31"
                },
                ...
            },
            ...
        ]
    """
    current_date = datetime.now().strftime('%Y-%m-%d')
    surveys = list(surveys_collection.find({
        'date.end': {'$lte': current_date}
    }).sort('date.create', -1).limit(10))

    for survey in surveys:
        survey['_id'] = str(survey['_id'])

    return jsonify(surveys), 200


#####################################################
# Récupérer les 10 surveys les plus recement update
#####################################################
@api.route('/api/recentUpdateSurveys', methods=['GET'])
def get_recentUpdatedSurveys():
    """
    Récupère les 10 derniers sondages mis à jour, triés par date de création.

    La fonction effectue une recherche dans la collection des sondages pour obtenir
    les 10 sondages les plus récemment mis à jour. Elle trie les résultats par date
    de création et renvoie les informations sous forme de liste.

    Étapes de la fonction :
    - Récupère la date actuelle.
    - Recherche les sondages dont la date de mise à jour est inférieure ou égale à la date actuelle.
    - Trie les sondages par date de création, de la plus récente à la plus ancienne.
    - Limite la réponse aux 10 premiers sondages.
    - Convertit l'ObjectId en chaîne de caractères pour chaque sondage.

    Retourne :
        - 200 : Liste des 10 sondages les plus récents, avec leurs détails.
        - Chaque sondage contient les informations comme l'id, la question, la description, etc.

    Exemple de réponse :
    - Succès :
        [
            {
                "id": "<id_survey>",
                "description": "Description du sondage",
                "question": "Question posée",
                "date": {
                    "create": "2024-12-30",
                    "update": "2024-12-31"
                },
                ...
            },
            ...
        ]
    """
    current_date = datetime.now().strftime('%Y-%m-%d')
    surveys = list(surveys_collection.find({
        'date.update': {'$lte': current_date}
    }).sort('date.create', -1).limit(10))

    for survey in surveys:
        survey['_id'] = str(survey['_id'])

    return jsonify(surveys), 200


##################################
# Affiche les details d'un survey
##################################
@api.route('/api/showSurvey', methods=['POST'])
def showSurvey():
    """
    Affiche les détails d'un sondage spécifique à partir de son ID.

    La requête doit contenir un JSON avec le champ suivant :
    {
        "id": <id_du_survey>
    }

    Étapes de la fonction :
    - Vérifie la validité du JSON fourni.
    - Recherche le sondage correspondant à l'ID donné dans la collection MongoDB.
    - Récupère les champs suivants du sondage :
        - id : Identifiant du sondage.
        - description : Description du sondage.
        - question : Question du sondage.
        - results : Résultats du sondage, s'ils existent.

    Retourne :
        - 200 : Les détails du sondage sous forme de JSON.
        - 400 : Format de requête invalide.

    Exemple de réponse :
    - Succès :
        {
            "id": "<id_survey>",
            "description": "Description du sondage",
            "question": "Question posée",
            "results": "Résultats disponibles"
        }
    - Erreur :
        {"error": "Invalid JSON format"}
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Invalid JSON format'}), 400

    surveys = surveys_collection.find_one(
        {"id": data["id"]},  # Critère de recherche
        {'id': 1, 'description': 1, 'question': 1, 'results': 1}  # Projection
    )

    return jsonify(surveys), 200


################################
# Création d'un survey
################################
@api.route('/api/createSurveys', methods=['POST'])
def create_survey():
    """
    Crée un nouveau sondage (survey) dans la base de données.

    La requête doit contenir un JSON avec les champs suivants :
    {
        "creator_id": <id_du_créateur>,
        "question": <question_du_survey>,
        "choices": <liste_des_choix>,
        "start_date": <date_de_début>,
        "end_date": <date_de_fin>,
        "algo": <algorithme_pour_le_calcul_des_résultats>
    }

    Champs optionnels :
    - "description" : Description du sondage.

    Étapes de la fonction :
    - Vérifie la présence des champs requis dans le JSON.
    - Initialise les données du sondage, notamment les réponses et les résultats vides.
    - Enregistre le sondage dans la collection MongoDB.

    Remarque :
    - Les dates doivent être au format ISO 8601 (ex. : "YYYY-MM-DD").
    - Le champ "algo" doit correspondre à un algorithme implémenté pour traiter les résultats du sondage.

    Retourne :
        - 201 : Sondage créé avec succès, retourne l'ID du sondage.
        - 400 : Champs requis manquants ou format de requête invalide.

    Exemple de réponse :
    - Succès :
        {"id": "<id_survey>"}
    - Erreur :
        {"error": "Missing required fields"}
    """
    data = request.get_json()
    required_fields = ['creator_id', 'question', 'choices', 'start_date', 'end_date', 'algo']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    surveys = {
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

    result = surveys_collection.insert_one(surveys)
    return jsonify({'id': str(result.inserted_id)}), 201

################################
# Création d'un user
################################
@api.route('/api/register', methods=['POST'])
def register():
    """
    Crée un nouvel utilisateur dans la base de données.

    La requête doit contenir un JSON avec les champs suivants :
    {
        "pseudo": <pseudo_de_l_utilisateur>,
        "password": <mot_de_passe>,
        "password_confirm": <confirmation_du_mot_de_passe>,
        "date_of_birth": <date_de_naissance>,
        "addresse": <adresse>,
        "job": <emploi>
    }

    Étapes de la fonction :
    - Vérifie la présence des champs requis dans le JSON.
    - Vérifie si un utilisateur avec le même pseudo existe déjà.
    - Ajoute le nouvel utilisateur à la base de données.

    Remarque :
    - Le mot de passe est stocké en clair (non recommandé pour un environnement de production).

    Retourne :
        - 201 : Utilisateur créé avec succès, retourne l'ID de l'utilisateur.
        - 400 : Champs requis manquants ou format de requête invalide.
        - 409 : Conflit, le pseudo existe déjà dans la base de données.

    Exemple de réponse :
    - Succès :
        {"id": "<id_utilisateur>"}
    - Erreur :
        {"error": "pseudo already exists"}
    """
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


##############################################
# Login des utilisateurs
##############################################
@api.route('/api/login', methods=['POST'])
def login():
    """
    Authentifie un utilisateur et génère un token JWT.

    La requête doit contenir un JSON au format suivant :
    {
        "pseudo": <pseudo_de_l_utilisateur>,
        "password": <mot_de_passe_de_l_utilisateur>
    }

    Étapes de la fonction :
    - Valide le format JSON de la requête.
    - Vérifie la présence des champs requis : "pseudo" et "password".
    - Recherche l'utilisateur correspondant dans la base de données.
    - Compare le mot de passe fourni avec celui stocké dans la base.
    - Si l'utilisateur est authentifié, génère un token JWT avec les informations utilisateur (sans le mot de passe).

    Retourne :
        - 200 : Authentification réussie avec un token JWT et les informations utilisateur.
        - 400 : Requête invalide ou champs manquants.
        - 401 : Identifiants invalides (pseudo ou mot de passe incorrect).
        - 500 : Erreur interne du serveur.

    Exemples de réponses :
    - Succès :
        {
            "message": "Success",
            "token": <token_jwt>,
            "user": {
                "pseudo": <pseudo>,
                "age": <age>,
                "address": <address>,
                "job": <job>,
                "admin": <admin>
            }
        }
    - Erreur :
        {"error": "Invalid JSON format"}
    """
    try:
        # Récupérer les données dans un JSON
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON format'}), 400

        # Vérif les champs requis
        required_fields = ['pseudo', 'password']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        # Vérif user infos (password et pseudo)
        user = users_collection.find_one({'pseudo': data['pseudo']})
        if not user or user['password'] != data['password']:
            return jsonify({'error': 'Invalid pseudo or password'}), 401

        # Préparer les datas des users (sans le mot de passe)
        user_data = {
            'pseudo': user['pseudo'],
            'age': user.get('age'),
            'address': user.get('address'),
            'job': user.get('job'),
            'admin': user.get('admin', False),
        }

        # token JWT
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


##################################
# Calcule le résultat d'un survey
##################################
@api.route('/api/calculateSurvey', methods=['POST'])
def calculate_survey():
    """
    Calcule le résultat d'un scrutin à l'aide de l'algorithme spécifié dans le survey.

    La requête doit contenir un JSON au format suivant :
    {
        "id": <id_du_survey>
    }

    Conditions pour le calcul :
    - Le scrutin doit être terminé (la date de fin doit être passée).

    Algorithmes supportés :
    - "condorcy" : Méthode Condorcet.
    - "majority" : Système de majorité simple.
    - "quantitySort" : Tri basé sur la quantité.

    Returns:
        Response:
            - 201 : Résultat calculé et sauvegardé avec succès.
            - 400 : Format JSON invalide.
            - 403 : Calcul non autorisé si la date de fin n'est pas encore passée.
            - 404 : Scrutin introuvable.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON format'}), 400

        # Recherche du scrutin dans la bdd
        survey = surveys_collection.find_one({"id": data["id"]})
        if not survey:
            return jsonify({'error': 'Survey not found'}), 404

        # Vérifier si la date de fin est passée
        if survey['date']['end'] < datetime.now().strftime('%Y-%m-%d'):
            return jsonify({'result': None, 'message': "Cannot calculate result before the survey ends"}), 403

        # Initialisation des modifications
        modifications = {
            "$set": {
                "result": None
            }
        }

        # Choix de l'algorithme
        match survey['algo']:
            case 'condorcy':
                modifications['$set']["result"] = Condorcy(survey['responses'])
            case 'majority':
                modifications['$set']["result"] = Majority(survey['responses'])
            case 'quantitySort':
                modifications['$set']["result"] = Quantity_Sort(survey['responses'])
            case _:
                return jsonify({'error': f"Unsupported algorithm: {survey['algo']}"}), 400

        # Mise à jour du résultat dans la bdd
        result = surveys_collection.update_one(
            {"id": data["id"]},
            modifications
        )

        return jsonify({'result': "Result calculated and saved successfully"}), 201

    except Exception as e:
        print(f"Erreur lors du calcul du résultat : {e}")
        return jsonify({'error': 'Internal Server Error'}), 500



#####################################
# Participation à un survey
#####################################
@api.route('/api/vote', methods=['POST'])
def vote():
    """
    Permet à un utilisateur de participer à un scrutin en soumettant sa réponse.

    La requête doit contenir un JSON au format suivant :
    {
        "id": <id_du_survey>,
        "data": {
            "response": <input_utilisateur>,
            "user_id": <id_de_l_utilisateur>
        }
    }

    Conditions de participation :
    - Le scrutin doit être actif (la date actuelle doit être entre la date de début et de fin).
    - Un utilisateur ne peut participer qu'une seule fois à un scrutin donné.

    Returns:
        Response:
            - 201 : Participation enregistrée ou messages d'erreur spécifiques.
            - 400 : Format JSON invalide.
    """
    try:
        data = request.get_json()  # Charger les données de la requête
        if not data:
            return jsonify({'error': 'Invalid JSON format'}), 400

        # Rechercher le scrutin
        survey = surveys_collection.find_one({"id": data["id"]})
        if not survey:
            return jsonify({'error': 'Survey not found'}), 404

        now = datetime.now().strftime('%Y-%m-%d')

        # Vérifier si le scrutin est actif
        if survey['date']['start'] <= now <= survey['date']['end']:
            # Vérifier si l'utilisateur a déjà participé
            for response in survey.get('reponses', []):
                if response["user_id"] == data['data']['user_id']:
                    return jsonify({'result': None, "message": "User already participated"}), 403

            # Ajouter la réponse
            modifications = {
                "$push": {
                    "reponses": data['data']
                }
            }
            surveys_collection.update_one({"id": data["id"]}, modifications)

            return jsonify({'result': "Data sent successfully"}), 201
        else:
            return jsonify({'result': None, 'message': "Cannot participate since the survey is not active"}), 403

    except Exception as e:
        print(f"Erreur lors de la participation au scrutin : {e}")
        return jsonify({'error': 'Internal Server Error'}), 500


##############################################
# Modification du survey si on est le créateur
##############################################
@api.route('/api/modify', methods=['POST'])
def modify():
    """
    Modifie un scrutin si l'utilisateur est le créateur et que les conditions de date le permettent.

    La requête doit contenir un JSON au format suivant :
    {
        "id": <id_du_survey>,
        "data": {
            "response": {
                "description": <str>,
                "question": <str>,
                "choix": <list>
            },
            "user_id": <id_de_l_utilisateur>
        }
    }

    Conditions de modification :
    - Le scrutin ne peut pas être modifié si sa date de fin ou sa date de début est passée.
    - Seul le créateur du scrutin peut effectuer des modifications.

    Returns:
        Response:
            - 201 : Succès ou messages d'erreur spécifiques selon les conditions.
            - 400 : Format JSON invalide.
    """
    try:
        data = request.get_json()  # Charger les données de la requête
        if not data:
            return jsonify({'error': 'Invalid JSON format'}), 400

        survey = surveys_collection.find_one({"id": data["id"]})
        if not survey:
            return jsonify({'error': 'Survey not found'}), 404

        now = datetime.now().strftime('%Y-%m-%d')

        if survey['date']['end'] < now or survey['date']['start'] < now:
            # Vérifier si l'utilisateur est le créateur
            if survey["creator"]["user_id"]["$oid"] != data['data']['user_id']:
                return jsonify({'result': None, "message": "User isn't the creator of the survey"}), 403

            # Filtrer les champs à modifier
            data_to_modify = {k: v for k, v in data['data']['response'].items() if v is not None}

            # Appliquer les modif
            modifications = {"$set": data_to_modify}
            surveys_collection.update_one({"id": data["id"]}, modifications)

            return jsonify({'result': "Modification done successfully"}), 200
        else:
            return jsonify({'result': None, 'message': "Cannot modify since the end date has passed or the starting date has started"}), 403

    except Exception as e:
        print(f"Erreur lors de la modification du scrutin : {e}")
        return jsonify({'error': 'Internal Server Error'}), 500


################################
# UC 10/11 - Dashboard Admin
################################

@api.route('/api/surveys/top-participants', methods=['GET'])
def top_surveys():
    """
    Récupère les scrutins ayant attiré le plus de participants.

    Returns:
        Response: Les données des scrutins sous forme JSON (code 200),
                  ou un message d'erreur en cas d'exception (code 500).
    """
    try:
        data = get_top_surveys_by_participants()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api.route('/api/surveys/<survey_id>/votes-by-birth-year', methods=['GET'])
def votes_by_year(survey_id):
    """
    Récupère la répartition des votes par année de naissance pour un scrutin donné.

    Args:
        survey_id (str): L'ID du scrutin.

    Returns:
        Response: Les données des votes par année de naissance sous forme JSON (code 200),
                  ou un message d'erreur si les données sont mal formatées ou en cas d'exception (code 500).
    """
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
    """
    Calcule le nombre moyen d'options disponibles par scrutin.

    Returns:
        Response: Un JSON contenant la moyenne des options (`average_choices`) (code 200),
                  ou un message d'erreur en cas d'exception (code 500).
    """
    try:
        data = get_average_choices()
        return jsonify({"average_choices": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api.route('/api/surveys/delete', methods=['DELETE'])
def delete_survey():
    """
    Supprime un scrutin basé sur son ID.

    La requête doit inclure un paramètre `survey_id` dans les arguments de la requête.

    Returns:
        Response: Un message confirmant la suppression du scrutin (code 200),
                  ou un message d'erreur si l'ID est manquant (code 400),
                  si aucun scrutin correspondant n'est trouvé (code 404),
                  ou en cas d'erreur interne (code 500).
    """
    try:
        survey_id = request.args.get('survey_id')
        if not survey_id:
            return jsonify({"error": "Missing survey_id"}), 400

        # Convertir survey_id en ObjectId pour chercher par _id
        result = surveys_collection.delete_one({"_id": ObjectId(survey_id)})
        if result.deleted_count == 1:
            return jsonify({"message": "Survey deleted successfully"}), 200
        else:
            return jsonify({"error": "Survey not found"}), 404
    except Exception as e:
        print(f"Erreur lors de la suppression du scrutin : {e}")
        return jsonify({"error": "An error occurred"}), 500


###################################################
# UC 3 - Modification de Profile
###################################################
@api.route('/api/account/<pseudo>', methods=['GET'])
def get_user(pseudo):
    """
    Docstring:
    Récupère les informations d'un utilisateur par son pseudo.

    Args:
        pseudo (str): Le pseudo de l'utilisateur à rechercher.

    Returns:
        Response: Les informations de l'utilisateur sous forme JSON si trouvé (code 200),
                  ou un message d'erreur si non trouvé (code 404) ou en cas d'erreur interne (code 500).
    """
    try:
        user = users_collection.find_one({'pseudo': pseudo})
        if not user:
            return jsonify({'error': 'User not found'}), 404

        user['_id'] = str(user['_id'])  # Convertir ObjectId en chaîne de caractères
        return jsonify(user), 200
    except Exception as e:
        print(f"Erreur lors de la récupération de l'utilisateur : {e}")
        return jsonify({'error': 'Internal Server Error'}), 500


@api.route('/api/account', methods=['PUT'])
def update_user():
    """
    Docstring:
    Met à jour les informations d'un utilisateur existant.

    La requête doit contenir un JSON avec les champs obligatoires suivants :
    - pseudo (str): Le pseudo de l'utilisateur à mettre à jour.
    - password (str): Le nouveau mot de passe de l'utilisateur.
    - date_of_birth (str): La nouvelle date de naissance de l'utilisateur.
    - addresse (str): La nouvelle adresse de l'utilisateur.
    - job (str): Le nouvel emploi de l'utilisateur.

    Returns:
        Response: Un message indiquant le nombre de documents modifiés (code 200),
                  ou un message d'erreur si les champs requis sont manquants (code 400),
                  si aucun document n'a été trouvé ou modifié (code 404),
                  ou en cas d'erreur interne (code 500).
    """
    try:
        data = request.get_json()
        required_fields = ['pseudo', 'date_of_birth', 'password', 'addresse', 'job']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        user = {
            'password': data['password'],
            'date_of_birth': data['date_of_birth'],
            'addresse': data['addresse'],
            'job': data['job'],
        }

        result = users_collection.update_one({'pseudo': data['pseudo']}, {'$set': user})
        if result.modified_count == 0:
            return jsonify({'error': 'No document found or no changes made'}), 404

        return jsonify({'modified_count': result.modified_count}), 200
    except Exception as e:
        print(f"Erreur lors du traitement de la requête: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500


###################################################
# UC 4 - Désactivation du Profil
###################################################
@api.route('/api/account', methods=['DELETE'])
def delete_user():
    """
    Supprime les informations d'un utilisateur de la base de données, à l'exception de son pseudo.

    Cette fonction récupère les informations envoyées dans la requête (en JSON), vérifie que le champ 'pseudo'
    est présent, puis met à jour les informations de l'utilisateur dans la collection MongoDB pour effacer
    son mot de passe, sa date de naissance, son adresse, son travail et son statut d'administrateur. L'utilisateur
    est ainsi désactivé sans supprimer son identifiant.

    La fonction répond par un message de succès si l'utilisateur a été mis à jour, sinon, elle retourne une erreur.

    Returns:
        jsonify: Si l'utilisateur a été mis à jour, retourne un message de confirmation.
        400: Si le champ 'pseudo' est manquant dans la requête.
        500: En cas d'erreur interne lors du traitement de la requête.
    """
    try:
        data = request.get_json()

        # Vérification des champs requis
        required_fields = ['pseudo']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        # Mise à jour de l'utilisateur (effacement des informations sensibles)
        users_collection.update_one({'pseudo': data['pseudo']}, {'$set': {'password': '',
                                                                          'date_of_birth': '',
                                                                          'addresse': '',
                                                                          'job': '',
                                                                          'admin': False}})

        return jsonify({'utilisateur effacé'}), 200

    except Exception as e:
        print(f"Erreur lors du traitement de la requête: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500
