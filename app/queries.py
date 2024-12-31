# requèete MongoDB pour UC10/11
from pymongo import MongoClient
from config import Config
from bson.objectid import ObjectId

client = MongoClient(Config.MONGO_URI)
db = client['condorcy']

# Collections
users_collection = db['users']
surveys_collection = db['surveys']

#Graph 1
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

# Graph 2
def get_votes_by_birth_year(survey_id):
    survey = surveys_collection.find_one({"_id": ObjectId(survey_id)})
    if not survey:
        return {"error": "Survey not found"}
    user_ids = []
    for response in survey["reponses"]:
        user_id = response["user_id"]
        if isinstance(user_id, dict) and "$oid" in user_id:
            user_ids.append(user_id["$oid"])
        else:
            user_ids.append(user_id)
    print("User IDs après correction :", user_ids)
    users = users_collection.find({"id": {"$in": user_ids}})
    users = list(users)
    print("Utilisateurs récupérés :", users)

# sysème de calcule des votes par rapport aux années de naissance (ne pas le toucher par pitié)
    birth_year_votes = {}
    for user in users:
        birth_year = int(user["date_of_birth"].split("-")[0])  # on va chercher l'année de naissance
        birth_year_votes.setdefault(birth_year, 0)  # on remet à 0 pour bien partir

    # on parcours chaque réponse pour incrémenter les votes
    for response in survey["reponses"]:
        response_user_id = str(response["user_id"].get("$oid", response["user_id"]))

        matching_user = next((user for user in users if str(user["id"]) == response_user_id), None)

        if matching_user:
            birth_year = int(matching_user["date_of_birth"].split("-")[0])
            birth_year_votes[birth_year] += len(response["reponse"])
    return birth_year_votes

# Graph 3
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
