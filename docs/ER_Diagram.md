# Intelligent Document Management System - ER Diagram

## Users Table

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| user_id | INTEGER | Primary Key (Unique User ID) |
| username | TEXT | Name of the user |
| email | TEXT | User email address |
| password | TEXT | Encrypted password |

---

## Documents Table

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| document_id | INTEGER | Primary Key |
| user_id | INTEGER | Foreign Key → Users.user_id |
| file_name | TEXT | Uploaded file name |
| category_id | INTEGER | Foreign Key → Categories.category_id |
| upload_date | DATE | Upload timestamp |
| extracted_text | TEXT | OCR extracted content |

---

## Categories Table

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| category_id | INTEGER | Primary Key |
| category_name | TEXT | Type of document |

---

## Activity Logs Table

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| log_id | INTEGER | Primary Key |
| user_id | INTEGER | Foreign Key → Users.user_id |
| action | TEXT | Action performed |
| timestamp | DATETIME | Action time |