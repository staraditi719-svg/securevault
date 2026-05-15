# 🔐 SecureVault

A full-stack Role-Based Access Control (RBAC) web application where different users get different levels of access — just like real enterprise security systems.

Built this project to understand how companies like HENNGE protect their internal tools and data using identity and access management.

---

## 🌐 Live Demo

- **Frontend:** https://securevault-amber.vercel.app
- **Backend API:** https://securevault-qci0.onrender.com
- **API Docs:** https://securevault-qci0.onrender.com/docs

---

## 💡 What is SecureVault?

Most real-world applications don't give every user the same permissions. A regular employee shouldn't be able to delete users or access system settings — only admins should. SecureVault demonstrates exactly this concept.

When you register, you get assigned a role. Based on that role, you can only access certain parts of the application. Try logging in as an admin vs a viewer — you'll see a completely different experience.

---

## 👥 Roles & Permissions

| Role    | What They Can Access                          |
|---------|-----------------------------------------------|
| Admin   | User management, all files, settings, analytics, admin panel |
| Editor  | Edit files, view files, analytics             |
| Viewer  | View files only                               |

---

## 🛠️ Tech Stack

**Backend**
- Python + FastAPI
- JWT (JSON Web Tokens) for authentication
- SQLAlchemy + SQLite for database
- Bcrypt for password hashing

**Frontend**
- React + TypeScript
- Vite for build tooling
- Axios for API calls
- React Router for navigation

**Deployment**
- Backend → Render
- Frontend → Vercel

---

## 🔒 Security Features

- Passwords are never stored as plain text — bcrypt hashing is used
- JWT tokens expire after 30 minutes for security
- Protected routes on both frontend and backend
- CORS configured to only allow requests from the official frontend
- Environment variables used for all secrets — nothing hardcoded

---

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/staraditi719-svg/securevault.git
cd securevault
```

**2. Set up backend**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file inside `/backend`:
```
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Run the backend:
```bash
uvicorn main:app --reload
```

**3. Set up frontend**
```bash
cd frontend
npm install
```

Create a `.env` file inside `/frontend`:
```
VITE_API_URL=http://localhost:8000
```

Run the frontend:
```bash
npm run dev
```

---

## 📁 Project Structure

```
securevault/
├── backend/
│   ├── main.py          # All API routes
│   ├── auth.py          # JWT logic, password hashing
│   ├── database.py      # Database connection and queries
│   ├── models.py        # Request/response models
│   └── requirements.txt
├── frontend/
│   └── src/
│       ├── pages/
│       │   ├── Login.tsx      # Login and Register page
│       │   ├── Dashboard.tsx  # Main dashboard
│       │   └── Admin.tsx      # Admin panel
│       ├── context/
│       │   └── AuthContext.tsx # Global auth state
│       └── App.tsx
└── README.md
```

---

## 🧠 What I Learned

- How JWT authentication works end to end
- Why role-based access control matters in real applications
- How to connect a React frontend to a FastAPI backend
- Deploying a full-stack app with proper environment variable management
- Debugging CORS errors and React hydration issues in production

---

## 🙋‍♀️ About

Made by **Aditi** — a third-year BTech student passionate about AI and full-stack development, currently building projects for international internship applications.

GitHub: [@staraditi719-svg](https://github.com/staraditi719-svg)
