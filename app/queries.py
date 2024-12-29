# requèete MongoDB pour UC10/11
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

client = MongoClient("mongodb://mongodb:27017/")
db = client["condorcy"]
surveys_collection = db["surveys"]
users_collection = db["users"]

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
    survey = surveys_collection.find_one({"_id": ObjectId(survey_id)})
    user_ids = [response["user_id"] for response in survey["reponses"]]
    users = users_collection.find({"_id": {"$in": user_ids}})
    current_year = datetime.now().year
    age_to_birth_year = {user["_id"]: current_year - user["age"] for user in users}

    birth_year_votes = {}
    for response in survey["reponses"]:
        birth_year = age_to_birth_year[response["user_id"]]
        birth_year_votes.setdefault(birth_year, [])
        birth_year_votes[birth_year].extend(response["reponse"])

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
