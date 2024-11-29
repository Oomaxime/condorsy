from pymongo import MongoClient

client = MongoClient('mongodb://root:pass@mongodb:27017/condorsy')

db = client['condorsy']
collection = db[''] #Mettre le nom de la collection quand vous l'aurez créé

def add_document(data):
    result = collection.insert_one(data)
    return str(result.inserted_id)

def get_all_documents():
    documents = list(collection.find())
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    return documents

# w...