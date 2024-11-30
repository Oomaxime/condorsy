from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html', title='Accueil')

@main_bp.route('/login')
def login():
    return render_template('login.html', title='Login')
