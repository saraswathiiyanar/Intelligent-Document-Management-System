# 🏗️ Technical Architecture – IDMS

## 1. System Overview
Intelligent Document Management System (IDMS) is a Flask-based web application for managing documents efficiently.

---

## 2. Architecture Flow

User
 │
 ▼
Flask Backend (REST API)
 │
 ├── Authentication Module
 ├── Document Module
 ├── User Module
 │
 ▼
Database (SQLite / MySQL)
 │
 ▼
File Storage (Uploads Folder)

---

## 3. Data Flow

User Request → Flask API → Validation → DB Operation → File Storage → JSON Response

---

## 4. Modules

### Authentication
- Login
- Register

### Document Management
- Upload file
- View files
- Delete file

### User Management
- User data store
- Document mapping

---

## 5. Database

Users Table:
- id
- name
- email

Documents Table:
- id
- filename
- user_id

---

## 6. Storage
- Local uploads folder
- Future: Cloud storage

---

## 7. Tech Stack
- Python (Flask)
- SQLAlchemy
- SQLite
- Postman
- Git

---

## 8. Future Scope
- OCR
- Search system
- Role-based access
- Cloud integration