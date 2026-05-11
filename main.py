from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from models import UserRegister, UserLogin, Token
from database import get_user, create_user
from auth import hash_password, verify_password, create_access_token, decode_token

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# ── Register endpoint ──
@app.post("/register")
def register(user: UserRegister):
    if get_user(user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed = hash_password(user.password)
    create_user(user.username, hashed, user.role)
    return {"message": f"User '{user.username}' registered successfully"}

# ── Login endpoint ──
@app.post("/login", response_model=Token)
def login(user: UserLogin):
    db_user = get_user(user.username)
    if not db_user or not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token({"sub": user.username, "role": db_user["role"]})
    return {"access_token": token, "token_type": "bearer"}

# ── Protected route example ──
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

def get_resources_by_role(role: str):
    resources = {
        "admin": ["user-management", "all-files", "settings", "analytics"],
        "editor": ["edit-files", "view-files", "analytics"],
        "viewer": ["view-files"]
    }
    return resources.get(role, [])