# System Design - Intelligent Document Management System (IDMS)

## 1. Overview
The system is designed using a layered architecture that includes UI, backend processing, AI modules, and storage.

## 2. Architecture

User → Web Interface → Flask Backend → OCR/NLP Engine → Database

## 3. Modules

### 3.1 User Module
Handles authentication and user management.

### 3.2 Document Upload Module
Allows users to upload files.

### 3.3 OCR Module
Converts images and scanned documents into text.

### 3.4 NLP Module
Processes extracted text for classification and search.

### 3.5 Search Module
Enables keyword-based document search.

## 4. Technologies Used
- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- OCR: Tesseract
- Database: MySQL / MongoDB