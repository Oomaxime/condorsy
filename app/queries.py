# requèete MongoDB pour UC10/11
from pymongo import MongoClient
from config import Config
from bson.objectid import ObjectId

client = MongoClient(Config.MONGO_URI)
db = client['condorcy']

# Collections
users_collection = db['users']
surveys_collection = db['surveys']


def get_top_surveys_by_participants():
    pipeline = [
        {"$unwind": "$reponses"},
        {"$group": {
            "_id": "$_id",
            "question": {"$first": "$question"},
            "participant_count": {"$sum": 1}
        }},
        {"$sort": {"participant_count": -1}}
    ]
    surveys = list(surveys_collection.aggregate(pipeline))

    # Convertir les _id MongoDB en chaîne de caractères pour faciliter le traitement côté frontend
    for survey in surveys:
        survey["_id"] = str(survey["_id"])

    return surveys


def get_votes_by_birth_year(survey_id):
    # survey_id est un ObjectId valide
    if isinstance(survey_id, str):
        survey_id = ObjectId(survey_id)
    survey = surveys_collection.find_one({"_id": survey_id})
    if not survey:
        return {"error": "Survey not found"}
    user_ids = [response["user_id"] for response in survey["reponses"]]
    try:
        user_ids = [ObjectId(user_id) if isinstance(user_id, str) else user_id for user_id in user_ids]
    except Exception as e:
        return {"error": f"Invalid user_id format: {e}"}
    if not user_ids:
        return {"error": "No participants found for this survey"}
    print(f"user_ids (avant requête): {user_ids}")

    try:
        users = users_collection.find({"_id": {"$in": user_ids}})
    except Exception as e:
        return {"error": f"Erreur dans la requête MongoDB : {e}"}

    # Calcul des votes par année de naissance
    birth_year_votes = {}
    for user in users:
        # Extraction de l'année de naissance
        birth_year = user["date_of_birth"].year
        birth_year_votes.setdefault(birth_year, [])
        for response in survey["reponses"]:
            if response["user_id"] == user["_id"]:
                birth_year_votes[birth_year].append(response["reponse"])

    # Convertir les votes en comptage (nombre de votes par années)
    birth_year_counts = {year: len(votes) for year, votes in birth_year_votes.items()}

    return birth_year_counts


def get_average_choices():
    pipeline = [
        {"$project": {"choice_count": {"$size": "$choix"}}},
        {"$group": {
            "_id": None,
            "average_choices": {"$avg": "$choice_count"}
        }}
    ]
    result = surveys_collection.aggregate(pipeline)
    return result.next()["average_choices"]
