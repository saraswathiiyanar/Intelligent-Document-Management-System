import os
import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    return conn


@app.route('/')
def home():
    return redirect('/login')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db()
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        conn.close()

        return "Registered successfully"

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()
        conn.close()

        if user:
            return redirect('/dashboard')
        else:
            return "Invalid Username or Password"

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['document']

        if file:
            os.makedirs("uploads", exist_ok=True)
            file.save(os.path.join("uploads", file.filename))
            return "File Uploaded Successfully"

    return render_template('upload.html')

@app.route('/documents')
def documents():
    files = os.listdir("uploads")
    return render_template('documents.html', files=files)

@app.route('/delete/<filename>')
def delete_file(filename):
    file_path = os.path.join("uploads", filename)

    if os.path.exists(file_path):
        os.remove(file_path)

    return redirect('/documents')

@app.route('/logout')
def logout():
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)