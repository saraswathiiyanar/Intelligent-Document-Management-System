# Intelligent Document Management System - API Documentation

---

## 🔐 Authentication APIs

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| POST | /register | Register new user | Success / Error message |
| POST | /login | User login | JWT Token / Error |

---

## 📄 Document APIs

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| POST | /upload | Upload document | Upload success |
| GET | /documents | Get all documents | List of documents |
| GET | /document/<id> | Get single document | Document details |
| DELETE | /document/<id> | Delete document | Delete confirmation |

---

## 📂 Category APIs

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| POST | /category | Create category | Created success |
| GET | /categories | Get all categories | List of categories |

---

## 🔎 Search API

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| GET | /search | Search documents | Matching documents |

---

## 📊 OCR API

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| POST | /ocr | Extract text from document | Extracted text |