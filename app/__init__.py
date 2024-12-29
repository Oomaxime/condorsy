from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'dev'

    from .routes import main_bp
    from .api import api

    app.register_blueprint(main_bp)
    app.register_blueprint(api)

    return app
