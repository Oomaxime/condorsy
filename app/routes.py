from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html', title='login')

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html', title='register')

@main_bp.route('/login')
def login():
    return render_template('old/login.html', title='Login')

@main_bp.route('/surveys/create', methods=['GET'])
def create_survey():
    return render_template('surveys/create.html')

@main_bp.route('/account')
def account():
    return render_template('account.html', title='Account')
  
@main_bp.route('/home')
def home():
    return render_template('base.html', title='home')

@main_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='dashboard')