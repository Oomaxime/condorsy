from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SECRET_KEY'] = 'dev'

    # Configuration JWT
    app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key'
    jwt = JWTManager(app)

    from .routes import main_bp
    from .api import api

    app.register_blueprint(main_bp)
    app.register_blueprint(api)

    return app