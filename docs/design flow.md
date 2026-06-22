# Design Flow – Intelligent Document Management System (IDMS)

## 🔷 Overview
This document describes the basic design flow of the Intelligent Document Management System (IDMS).

## 🔷 System Flow

1. **User Login / Registration**
   - User creates an account or logs into the system
   - Authentication is verified before access

2. **Document Upload**
   - User uploads documents (image / PDF)
   - File is sent to the backend server

3. **OCR Processing**
   - Uploaded document is processed using OCR
   - Text is extracted from images/PDF files

4. **Data Extraction**
   - Extracted text is cleaned and structured
   - Important information is identified

5. **Storage**
   - Processed data is stored in the database
   - Original file is also saved securely

6. **Retrieval**
   - User can search and view stored documents
   - Extracted text is displayed for easy access

## 🔷 System Architecture Flow
Frontend (HTML/CSS) → Backend (Flask/Python) → OCR Engine → Database

## 🔷 Summary
The system ensures smooth document handling by combining upload, OCR processing, and structured storage for easy retrieval.