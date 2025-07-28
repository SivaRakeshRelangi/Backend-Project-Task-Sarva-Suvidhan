# 🚆 KPA Form API

A FastAPI-based backend service to manage submission and retrieval of **Wheel Specification** forms, backed by PostgreSQL. This system is designed to dynamically store form fields in JSON format and is optimized for easy deployment with Docker.

---

## 📦 Features

- ✅ Submit new wheel specification forms (`POST`)
- 🔍 Filter and retrieve forms (`GET`)
- 🗃️ JSON-based flexible form schema
- 🔄 Live reload during development
- 🐳 Dockerized setup (FastAPI + PostgreSQL)
- 📄 Environment-based config with `.env`

---

## 🚀 Quick Start (with Docker)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/kpa_backend.git
cd kpa_backend
```

### 2️⃣ Set Up Environment
Create a .env file in the root directory:
```bash
DATABASE_URL=postgresql://postgres:postgres@db:5432/kpa_db

```

### 3️⃣ Start Services
```bash
docker-compose up --build
```

This will:

- Build the FastAPI app container
- Start PostgreSQL with persistence
- Auto-restart services if they fail

# 🧰 Tech Stack
| Layer      | Technology             |
| ---------- | ---------------------- |
| Backend    | FastAPI                |
| ORM        | SQLAlchemy             |
| DB         | PostgreSQL             |
| Env Config | python-dotenv          |
| Container  | Docker, Docker Compose |
