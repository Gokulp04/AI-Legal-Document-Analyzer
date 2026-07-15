# AI-LEGAL DOCUMENT ANALYZER

## Abstract

The AI Legal Document Analyzer is a web-based application developed to simplify the analysis of legal documents using Artificial Intelligence. The system allows users to upload legal PDF documents such as contracts, agreements, and policies. It automatically extracts text from the uploaded documents, generates AI-powered summaries, answers user questions related to the document, and provides downloadable legal analysis reports.

The application reduces the time and effort required to understand lengthy legal documents while improving accessibility through an intelligent and user-friendly interface. It also maintains document history, provides dashboard statistics, and includes an admin panel for managing users and uploaded documents.

---

# Objectives

- Automate the legal document analysis process.
- Extract text from uploaded PDF documents.
- Generate AI-powered summaries.
- Answer user queries about uploaded documents.
- Generate downloadable legal analysis reports.
- Maintain document upload history.
- Provide dashboard statistics.
- Implement secure user authentication.
- Manage users and documents through an admin panel.

---

# Requirement Analysis

## Inputs

### User Details

Users register and log in using:

- Name
- Email
- Password

### Legal Documents

Users upload legal PDF files.

Examples:

- Employment_Contract.pdf
- Rental_Agreement.pdf
- Company_Policy.pdf
- NDA_Document.pdf
- Service_Agreement.pdf

### User Questions

Example:

- What is the contract duration?
- What is the salary mentioned?
- Who are the parties involved?
- Is there any penalty clause?

---

# Outputs

The system generates:

- AI Summary
- Key Legal Information
- AI Question & Answer
- Downloadable PDF Report
- Document History
- Dashboard Statistics
- Admin Panel Reports

---

# Front End Details

## Technologies Used

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Font Awesome

## Features

- User Registration
- User Login
- Dashboard
- Upload Legal PDF
- AI Summary Page
- Ask AI Interface
- Download Report
- Document History
- Admin Dashboard

---

# Back End Details

## Technologies Used

- Python
- Flask
- SQLite
- Google Gemini AI
- PyMuPDF (fitz)
- PyPDF2
- ReportLab

## Backend Functions

- User Authentication
- PDF Upload
- Text Extraction
- AI Summary Generation
- AI Question Answering
- Report Generation
- Database Storage
- Dashboard Statistics
- Admin Management

---

# Database Details

## Database Name

```
legal_documents.db
```

## Table 1

### User

| Field Name | Type | Description |
|------------|------|-------------|
| id | INTEGER | Primary Key |
| name | TEXT | User Name |
| email | TEXT | Email Address |
| password | TEXT | Encrypted Password |
| is_admin | BOOLEAN | Admin Access |

---

## Table 2

### Document

| Field Name | Type | Description |
|------------|------|-------------|
| id | INTEGER | Primary Key |
| filename | TEXT | PDF File Name |
| summary | TEXT | AI Generated Summary |
| upload_date | TEXT | Upload Date |
| user_id | INTEGER | Foreign Key |

---

# System Modules

## Module 1: User Authentication Module

Allows users to register and log into the system securely.

---

## Module 2: PDF Upload Module

Uploads legal PDF documents.

---

## Module 3: PDF Text Extraction Module

Extracts text from uploaded legal documents.

---

## Module 4: AI Summary Module

Generates concise legal summaries using Google Gemini AI.

---

## Module 5: AI Question Answering Module

Answers user questions based on the uploaded document.

---

## Module 6: Report Generation Module

Creates downloadable AI-generated PDF reports.

---

## Module 7: Document History Module

Stores all uploaded documents with summaries.

---

## Module 8: Dashboard Module

Displays live statistics and recent uploads.

---

## Module 9: Admin Panel Module

Allows administrators to manage users and uploaded documents.

---

# Algorithm

### Step 1

Register/Login into the application.

### Step 2

Upload a legal PDF document.

### Step 3

Extract text from the uploaded PDF.

### Step 4

Send extracted text to Google Gemini AI.

### Step 5

Generate an AI-powered legal summary.

### Step 6

Display the analysis result.

### Step 7

Allow users to ask questions.

### Step 8

Generate AI answers.

### Step 9

Store document details in SQLite.

### Step 10

Display document history.

### Step 11

Generate downloadable PDF report.

### Step 12

Admin monitors users and uploaded documents.

---

# System Workflow

```
User Login
      ↓
Upload Legal PDF
      ↓
Extract PDF Text
      ↓
Google Gemini AI
      ↓
Generate Summary
      ↓
Ask AI Questions
      ↓
Generate AI Answer
      ↓
Download Report
      ↓
Save Document History
      ↓
Dashboard & Admin Panel
```

---

# Sample Output

| Document | Status |
|----------|---------|
| Employment_Contract.pdf | Analyzed ✅ |
| Rental_Agreement.pdf | Completed ✅ |
| Company_Policy.pdf | Completed ✅ |
| NDA_Document.pdf | Processing ⏳ |

---

# Features

- Secure Authentication
- AI Legal Summary
- AI Question Answering
- PDF Upload
- Download Report
- Dashboard Statistics
- Document History
- Admin Panel
- SQLite Database

---

# Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Bootstrap
- JavaScript
- SQLite
- Google Gemini AI
- PyMuPDF
- PyPDF2
- ReportLab

---

# Future Enhancements

- OCR Support for Scanned PDFs
- Multi-language Legal Analysis
- Clause Risk Detection
- Legal Compliance Checker
- Cloud Storage Integration
- Email Notifications
- Voice-based AI Assistant
- Role-Based Access Control

---

# Conclusion

The AI Legal Document Analyzer provides an intelligent solution for understanding complex legal documents. By integrating Artificial Intelligence with PDF processing and a user-friendly web interface, the system enables users to generate legal summaries, ask document-related questions, download AI reports, and manage uploaded documents efficiently. The project minimizes manual effort, saves time, and improves accessibility to legal information.

---

# Developed By

**Gokul P**
