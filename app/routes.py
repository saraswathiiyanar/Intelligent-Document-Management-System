from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return redirect(url_for('main.login'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "admin" and password == "admin":
            return redirect(url_for('main.dashboard'))

        return "Invalid Username or Password"

    return render_template('login.html')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@main.route('/upload')
def upload():
    return render_template('upload.html')

@main.route('/documents')
def documents():
    return render_template('documents.html')

@main.route('/logout')
def logout():
    return redirect(url_for('main.login'))