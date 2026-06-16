from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Intelligent Document Management System (IDMS)"

@app.route("/login")
def login():
    return "Login Page"

@app.route("/dashboard")
def dashboard():
    return "Dashboard Page"

if __name__ == "__main__":
    app.run(debug=True)