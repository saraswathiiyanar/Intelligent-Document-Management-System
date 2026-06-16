# Database Design - Intelligent Document Management System (IDMS)

## 1. Overview
The database stores user information, documents, and extracted text data.

## 2. Tables

### 2.1 Users Table
| Field      | Type         | Description          |
|------------|-------------|----------------------|
| id         | INT (PK)     | Unique user ID       |
| name       | VARCHAR      | User name            |
| email      | VARCHAR      | User email           |
| password   | VARCHAR      | Hashed password      |

---

### 2.2 Documents Table
| Field        | Type         | Description              |
|--------------|-------------|--------------------------|
| doc_id       | INT (PK)     | Document ID              |
| user_id      | INT (FK)     | Uploaded user            |
| filename     | VARCHAR      | File name                |
| file_path    | VARCHAR      | Storage location        |
| upload_date  | TIMESTAMP    | Upload time              |

