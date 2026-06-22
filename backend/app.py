import sys
import os

sys.path.append(os.path.abspath(".."))
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

from ocr.ocr_engine import extract_text 

app = Flask(__name__, template_folder="../templates")

@app.route("/")
def home():
   return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return "Dashboard Page"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db()
        conn.execute(
            'INSERT INTO users (username, password) VALUES (?, ?)',
            (username, password)
        )
        conn.commit()
        conn.close()

        return "Registered successfully"

    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)