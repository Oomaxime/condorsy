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
    return list(surveys_collection.aggregate(pipeline))


def get_votes_by_birth_year(survey_id):
    # Récupération du scrutin spécifié
    survey = surveys_collection.find_one({"_id": ObjectId(survey_id)})
    if not survey:
        return {"error": "Survey not found"}

    # Récupération des utilisateurs ayant participé
    user_ids = [response["user_id"] for response in survey["reponses"]]
    users = users_collection.find({"_id": {"$in": user_ids}})

    # Calcul des votes par année de naissance
    birth_year_votes = {}
    for user in users:
        birth_year = user["date_of_birth"].year
        birth_year_votes.setdefault(birth_year, 0)
        # Compter les réponses pour chaque année
        for response in survey["reponses"]:
            if response["user_id"] == user["_id"]:
                birth_year_votes[birth_year] += len(response["reponse"])

    return birth_year_votes


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
