# 📝 FastAPI Blog

A simple blog application built with **FastAPI** that supports CRUD operations on posts, user authentication, and user profiles.  
It provides both **web views** and **API endpoints** for flexibility.

---

## 🚀 Features
- ✍️ CRUD operations on blog posts (Create, Read, Update, Delete)
- 🔐 Authentication with JWT (register/login)
- 👤 User profiles (view and update)
- 🌐 Web views for blog and user pages
- 🔗 REST API endpoints for external clients

---

## 📂 Endpoints

### 🌐 Web Views
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Homepage showing all blog posts |
| `/posts/{id}` | GET | View a single blog post |
| `/login` | GET/POST | User login page |
| `/profile` | GET | User profile page |

### 🔗 API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/posts/` | GET | List all posts |
| `/api/posts/` | POST | Create a new post |
| `/api/posts/{id}` | GET | Retrieve a post by ID |
| `/api/posts/{id}` | PUT/PATCH | Update a post |
| `/api/posts/{id}` | DELETE | Delete a post |
| `/api/auth/register` | POST | Register a new user |
| `/api/auth/login` | POST | Login and get JWT token |
| `/api/users/me` | GET | Get current user profile |

---

## 🖼️ Demo

### Web View
![Web View Demo](static/readme/Screenshot%20from%202026-01-21%2015-55-05.png)

### API View
![API View Demo](static/readme/Screenshot%20from%202026-01-12%2021-06-07.png)

---

## 🛠️ Tech Stack
- **Python 3.12+**
- **FastAPI**
- **SQLite/Postgres**
- **JWT Authentication**
- **Jinja2 Templates** (for web views)

---

## ⚡ Quick Start
1. Install dependencies using [uv](https://github.com/astral-sh/uv): ```bash
uv pip install -r requirements.txt

## Run
uvicorn main:app --reload

## Visit:

Web view → http://127.0.0.1:8000/

API docs → http://127.0.0.1:8000/docs
API redoc → http://127.0.0.1:8000/redoc
