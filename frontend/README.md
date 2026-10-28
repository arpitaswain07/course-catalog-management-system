# Course Catalog Management System

A full-stack web application for browsing and managing courses, built with a React frontend, FastAPI backend, and MySQL database.

## Features

- Browse available courses from the backend API
- Search courses by course name, instructor, or description
- View additional information for individual courses
- REST API endpoints for course management
- MySQL database integration
- Responsive course catalog interface

## Technology Stack

**Frontend**
- React
- Vite
- JavaScript
- CSS

**Backend**
- Python
- FastAPI
- SQLAlchemy
- Pydantic

**Database**
- MySQL

**Tools**
- Git
- GitHub
- Visual Studio Code

## Project Structure

```text
course_catalog/
├── controllers/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── styles.css
│   ├── package.json
│   └── vite.config.js
├── database.py
├── main.py
├── models.py
├── schema.py
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.10 or a compatible version
- Node.js and npm
- MySQL Server
- Git

## Setup and Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd course_catalog
```

### 2. Configure the database

Create a MySQL database and configure the connection settings expected by `database.py`.

Keep database credentials in environment variables or a local `.env` file. Never commit passwords or secret keys.

### 3. Set up the backend

Create and activate a Python virtual environment, then install dependencies.

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Start the API:

```powershell
python -m uvicorn main:app --reload
```

Open the interactive API documentation at:

http://127.0.0.1:8000/docs

### 4. Set up the frontend

Open a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL displayed by Vite in your terminal.

## API Documentation

FastAPI provides interactive API documentation at `/docs` when the backend is running.

The available endpoints depend on the routes registered in the application.

## Current Status

The frontend has been tested for course loading, search filtering, course details toggling, and responsive layout. The frontend dependency audit reported zero vulnerabilities after `npm audit fix`.

Backend endpoint testing and complete application verification should be completed before describing the project as fully production-ready.

## Future Improvements

- Add course creation, editing, and deletion through the interface
- Add dedicated course detail pages
- Improve automated testing
- Add authentication and authorization
- Deploy the frontend and backend

## Author

Created as a full-stack software development project.
