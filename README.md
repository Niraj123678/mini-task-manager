# 🛠️ FastAPI Backend - Mini Task Manager

This is the backend for the Mini Task Manager app built using **FastAPI** and **SQLite**.

## ✅ Features

- Create, update, delete, and list tasks
- Pydantic-based request and response models
- Dependency injection using FastAPI's `Depends`
- Swagger documentation at `/docs`

## 🧱 Tech Stack

- FastAPI
- SQLite (via SQLAlchemy)
- Pydantic
- Uvicorn

## 🚀 Running the Backend

### 1. Create a virtual environment

```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
pip install fastapi uvicorn sqlalchemy pydantic[dotenv]
uvicorn main:app --reload
