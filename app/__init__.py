import os
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from pymongo import MongoClient
from config import Config

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SECRET_KEY'] = 'dev'

    # Utilisez une clé sécurisée pour le JWT
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'fallback-secret-key')

    jwt = JWTManager(app)

    from .routes import main_bp
    from .api import api

    app.register_blueprint(main_bp)
    app.register_blueprint(api)

    return app

try:
    client = MongoClient(Config.MONGO_URI)
    db = client['condorcy']
    # Si la connexion réussit, afficher un message
    print("Connexion à MongoDB réussie!")
except Exception as e:
    print("Erreur de connexion à MongoDB:", e)
