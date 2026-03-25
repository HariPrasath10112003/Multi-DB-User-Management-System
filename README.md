# Multi-DB User Management System

A full-stack web application that demonstrates authentication and user management using multiple databases.

---

## Features

- User Registration (MySQL)
- Login Authentication (MySQL)
- Session Management (Redis)
- Profile Management (MongoDB)
- AJAX-based frontend (no page reload)

---

## Tech Stack

### Frontend
- HTML
- CSS (Bootstrap)
- JavaScript (jQuery AJAX)

### Backend
- Python (Flask)

### Databases
- MySQL → Stores user credentials
- MongoDB → Stores user profile data
- Redis → Stores session information

---

## Application Flow

1. Register → User details stored in MySQL  
2. Login → Credentials verified from MySQL  
3. Session → Stored in Redis  
4. Profile → Stored/updated in MongoDB  
---

## How to Run

### 1. Start Databases
Make sure the following are running:
- MySQL
- MongoDB
- Redis

---

### 2. Run Backend

```bash
python app.py

