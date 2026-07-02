from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# 👤 User Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    # 🔗 Relationship
    documents = db.relationship('Document', backref='user', lazy=True)


# 📄 Document Table
class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    file_path = db.Column(db.String(300), nullable=False)
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)

    # 🔗 Foreign Key (Relationship link)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)