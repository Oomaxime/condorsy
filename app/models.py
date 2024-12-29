from pymongo import MongoClient
from config import Config
from datetime import datetime, UTC

client = MongoClient(Config.MONGO_URI)
db = client['condorcy']

# Collections
users_collection = db['users']
surveys_collection = db['surveys']

class Survey:
    def __init__(self, creator_id, question, description, choices, start_date, end_date):
        self.creator_id = creator_id
        self.question = question
        self.description = description
        self.choices = choices
        self.start_date = start_date
        self.end_date = end_date
        self.created_at = datetime.now(UTC)
        self.responses = []

try:
    client.server_info() #tentative de connexion
    print("Connexion réussie à MongoDB !")
except Exception as e:
    print(f"Erreur de connexion à MongoDB : {e}")
