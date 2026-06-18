from flask import Blueprint, render_template, request, redirect, url_for, session
from app.database import get_db

main = Blueprint('main', __name__)

# ---------------- HOME ----------------
@main.route('/')
def home():
    return redirect(url_for('main.login'))

# ---------------- LOGIN ----------------
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()
        conn.close()

        if user:
            session['user'] = username
            return redirect(url_for('main.dashboard'))

        return "Invalid Username or Password"

    return render_template('login.html')

# ---------------- DASHBOARD ----------------
@main.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', user=session['user'])
    return redirect(url_for('main.login'))

# ---------------- UPLOAD ----------------
@main.route('/upload')
def upload():
    if 'user' in session:
        return render_template('upload.html')
    return redirect(url_for('main.login'))

# ---------------- DOCUMENTS ----------------
@main.route('/documents')
def documents():
    if 'user' in session:
        return render_template('documents.html')
    return redirect(url_for('main.login'))

# ---------------- LOGOUT ----------------
@main.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('main.login'))