from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('base.html', title='Accueil')

@main_bp.route('/login')
def login():
    return render_template('login.html', title='Login')

@main_bp.route('/surveys/create', methods=['GET'])
def create_survey():
    return render_template('surveys/create.html')

# Ajoutez vos autres routes ici...
