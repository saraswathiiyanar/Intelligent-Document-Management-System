# Intelligent Document Management System (IDMS)
## API Documentation

This document defines the REST API endpoints used in the Intelligent Document Management System for handling authentication, document management, category management, and OCR processing.

---

# Authentication APIs

## User Registration
POST /api/auth/register

Registers a new user into the system.

Request Body:
{
  "username": "string",
  "email": "string",
  "password": "string"
}

Response:
{
  "message": "User registered successfully",
  "user_id": "integer"
}

---

## User Login
POST /api/auth/login

Authenticates user credentials and provides access.

Request Body:
{
  "email": "string",
  "password": "string"
}

Response:
{
  "message": "Login successful",
  "user_id": "integer"
}

---

# Document APIs

## Upload Document
POST /api/documents/upload

Uploads a document and processes OCR extraction.

Request (form-data):
file: document file
user_id: integer
category_id: integer

Response:
{
  "message": "Document uploaded successfully",
  "document_id": "integer",
  "extracted_text": "string"
}

---

## Get All Documents
GET /api/documents

Returns all uploaded documents.

Response:
[
  {
    "document_id": "integer",
    "file_name": "string",
    "upload_date": "date"
  }
]

---

## Get Document by ID
GET /api/documents/{id}

Returns details of a specific document.

Response:
{
  "document_id": "integer",
  "file_name": "string",
  "extracted_text": "string"
}

---

## Delete Document
DELETE /api/documents/{id}

Deletes a document from the system.

Response:
{
  "message": "Document deleted successfully"
}

---

# Category APIs

## Get All Categories
GET /api/categories

Returns all document categories.

Response:
[
  {
    "category_id": "integer",
    "category_name": "string"
  }
]

---

## Add Category
POST /api/categories/add

Adds a new document category.

Request Body:
{
  "category_name": "string"
}

Response:
{
  "message": "Category added successfully",
  "category_id": "integer"
}

---

# OCR API

## Extract Text
POST /api/ocr/extract

Extracts text from uploaded document using OCR engine.

Request (form-data):
file: document/image

Response:
{
  "extracted_text": "string"
}

---

# System Flow

User Login → Upload Document → OCR Processing → Store in Database → Retrieve / View / Delete Document

---

# End of API Documentation