# SecureVault

A full-stack Role-Based Access Control (RBAC) web app I built as part of my application for the HENNGE Global Internship Program. The idea was to simulate how enterprise tools like HENNGE ONE manage secure access to cloud resources — different users get different levels of access based on their role.

**Live demo:** https://securevault-amber.vercel.app  
**Backend API:** https://securevault-qci0.onrender.com/docs

---

## What it does

Users can register with one of three roles — admin, editor, or viewer. Once logged in, they see only the resources their role allows. Admins get access to an additional admin panel with system controls. The whole thing is protected with JWT tokens so you can't access anything without logging in first.

---

## Tech stack

**Backend**
- Python + FastAPI
- JWT authentication (via python-jose)
- Password hashing with bcrypt
- SQLite database using SQLAlchemy
- Pytest for testing (12 tests, all passing)

**Frontend**
- React + TypeScript
- Vite for bundling
- Axios for API calls
- React Router for navigation

**Infrastructure**
- Docker + docker-compose (containerized both services)
- GitHub Actions for CI/CD (runs tests on every push)
- Render for backend hosting
- Vercel for frontend hosting

---

## Project structure

```
securevault/
├── backend/
│   ├── main.py          # FastAPI app and routes
│   ├── auth.py          # JWT and password logic
│   ├── database.py      # SQLAlchemy models and helpers
│   ├── models.py        # Pydantic schemas
│   ├── requirements.txt
│   └── tests/
│       ├── test_auth.py
│       └── test_routes.py
├── frontend/
│   └── src/
│       └── pages/
│           ├── Login.tsx
│           ├── Dashboard.tsx
│           └── Admin.tsx
├── docker-compose.yml
└── .github/
    └── workflows/
        └── ci.yml
```

---

## How to run locally

**Backend**
```bash
cd backend
python -m venv venv
source venv/Scripts/activate   # Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend**
```bash
cd frontend
npm install
npm run dev
```

Then open http://localhost:5173 in your browser.

**Or with Docker**
```bash
docker-compose up --build
```

---

## API endpoints

| Method | Endpoint | Access |
|--------|----------|--------|
| POST | /register | Public |
| POST | /login | Public |
| GET | /dashboard | All logged-in users |
| GET | /admin | Admin only |
| GET | /editor | Admin + Editor |

---

## Role permissions

| Role | Resources |
|------|-----------|
| Admin | user-management, all-files, settings, analytics |
| Editor | edit-files, view-files, analytics |
| Viewer | view-files |

---

## Running tests

```bash
cd backend
pytest tests/ -v
```

All 12 tests cover registration, login, token validation, role-based access, and edge cases like duplicate users and wrong passwords.

---

## Deployment

The backend is deployed on Render and the frontend is deployed on Vercel, connected to each other over HTTPS.

CI/CD is set up with GitHub Actions — every push to main automatically runs the full test suite.

---

## Why I built this

I'm applying for the HENNGE Global Internship Program (Batch 4). HENNGE builds identity and access management tools for enterprises, and I wanted to build something that touches the same problem space — controlling who can access what, and making sure it's secure. SecureVault is my attempt at understanding that from the ground up.

Built by Aditi — 3rd year BTech student from Kanpur, India.
