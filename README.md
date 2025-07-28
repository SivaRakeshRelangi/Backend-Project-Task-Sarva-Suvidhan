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
git clone https://github.com/SivaRakeshRelangi/Backend-Project-Task-Sarva-Suvidhan.git
cd Backend-Project-Task-Sarva-Suvidhan
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

# 📑 API Endpoints
### ▶️ POST 
/api/forms/wheel-specifications

Submit a new form.

**Request Body** (JSON):

```bash
{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "wheelGauge": "1600 (+2,-1)"
  }
}
```
**Success Response (201):**
```bash
{
  "success": true,
  "message": "Wheel specification submitted successfully.",
  "data": {
    "formNumber": "WHEEL-2025-001",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03",
    "status": "Saved"
  }
}
```
### 🔍 GET 

http://localhost:8000/api/forms/wheel-specifications?formNumber=WHEEL-2025-012

**Query Parameters (Optional):**
- formNumber
- submittedBy
- submittedDate
**Example:**
```bash
GET /api/forms/wheel-specifications?formNumber=WHEEL-2025-001
```
**Success Response (200):**
```bash
[
  {
    "formNumber": "WHEEL-2025-001",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03",
    "fields": {
      "treadDiameterNew": "915 (900-1000)",
      "wheelGauge": "1600 (+2,-1)"
    }
  }
]

```

