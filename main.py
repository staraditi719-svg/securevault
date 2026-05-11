from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from models import UserRegister, UserLogin, Token
from database import get_user, create_user, get_db, init_db
from auth import hash_password, verify_password, create_access_token, decode_token

app = FastAPI()

# Create tables when app starts
init_db()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# ── Register endpoint ──
@app.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    existing_user = get_user(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed = hash_password(user.password)
    create_user(db, user.username, hashed, user.role)
    return {"message": f"User '{user.username}' registered successfully"}

# ── Login endpoint ──
@app.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user(db, user.username)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token({"sub": db_user.username, "role": db_user.role})
    return {"access_token": token, "token_type": "bearer"}

# ── Dashboard endpoint ──
@app.get("/dashboard")
def dashboard(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return {
        "message": f"Welcome {payload['sub']}!",
        "role": payload["role"],
        "resources": get_resources_by_role(payload["role"])
    }

# ── Admin only endpoint ──
@app.get("/admin")
def admin_panel(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    if payload["role"] != "admin":
        raise HTTPException(status_code=403, detail="Access denied — admins only")
    return {"message": "Welcome to admin panel!", "access": "full"}

# ── Editor only endpoint ──
@app.get("/editor")
def editor_panel(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    if payload["role"] not in ["admin", "editor"]:
        raise HTTPException(status_code=403, detail="Access denied — editors only")
    return {"message": "Welcome to editor panel!", "access": "edit files"}

def get_resources_by_role(role: str):
    resources = {
        "admin": ["user-management", "all-files", "settings", "analytics"],
        "editor": ["edit-files", "view-files", "analytics"],
        "viewer": ["view-files"]
    }
    return resources.get(role, [])