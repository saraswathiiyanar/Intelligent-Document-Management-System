# Intelligent Document Management System (IDMS)
## Entity Relationship Diagram Description

This document describes the database structure and relationships used in the Intelligent Document Management System. The system is designed to manage users, documents, categories, OCR extracted data, and activity logs in a structured relational format.

---

# 📌 Entities Overview

## 1. Users Entity
Represents all registered users in the system.

Attributes:
- user_id (Primary Key)
- username
- email
- password
- created_at

---

## 2. Documents Entity
Represents uploaded documents and extracted content.

Attributes:
- document_id (Primary Key)
- user_id (Foreign Key)
- category_id (Foreign Key)
- file_name
- upload_date
- extracted_text

---

## 3. Categories Entity
Represents classification types for documents.

Attributes:
- category_id (Primary Key)
- category_name

---

## 4. Activity Logs Entity
Represents user actions performed in the system.

Attributes:
- log_id (Primary Key)
- user_id (Foreign Key)
- action
- timestamp

---

# 🔗 Relationships

- USERS (1) ───────────────< DOCUMENTS (M)
- USERS (1) ───────────────< ACTIVITY_LOGS (M)
- CATEGORIES (1) ───────────< DOCUMENTS (M)

---

# Relationship Explanation

Each user can upload multiple documents and perform multiple actions. Each document belongs to one user and one category. Categories are used to group multiple documents under a single classification. Activity logs track all user operations for monitoring and auditing purposes.

---

# 📊 ER Structure Representation

USERS
  |
  | 1
  |
  ├──────────────< DOCUMENTS >──────────────┐
  |                                        |
  |                                        |
  └──────────────< ACTIVITY_LOGS           CATEGORIES (1)