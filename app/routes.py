from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html', title='Accueil')

@main_bp.route('/login')
def login():
    return render_template('old/login.html', title='Login')

@main_bp.route('/surveys/create', methods=['GET'])
def create_survey():
    return render_template('surveys/create.html')

# Ajoutez vos autres routes ici...


@main_bp.route('/account')
def account():
    return render_template('account.html', title='Account')