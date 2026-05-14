import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from main import app

# Use a separate test database so real data is not affected
TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create test tables
Base.metadata.create_all(bind=engine)

# Override the real database with test database
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# Test 1 — register a new user
def test_register_user():
    response = client.post("/register", json={
        "username": "testuser",
        "password": "testpass123",
        "role": "admin"
    })
    assert response.status_code == 200
    assert "registered successfully" in response.json()["message"]
    print("✅ test_register_user passed")

# Test 2 — register same user twice should fail
def test_register_duplicate_user():
    client.post("/register", json={
        "username": "duplicateuser",
        "password": "testpass123",
        "role": "viewer"
    })
    response = client.post("/register", json={
        "username": "duplicateuser",
        "password": "testpass123",
        "role": "viewer"
    })
    assert response.status_code == 400
    print("✅ test_register_duplicate_user passed")

# Test 3 — login with correct credentials
def test_login_success():
    client.post("/register", json={
        "username": "loginuser",
        "password": "testpass123",
        "role": "editor"
    })
    response = client.post("/login", json={
        "username": "loginuser",
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
    print("✅ test_login_success passed")

# Test 4 — login with wrong password
def test_login_wrong_password():
    response = client.post("/login", json={
        "username": "loginuser",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    print("✅ test_login_wrong_password passed")

# Test 5 — admin can access admin panel
def test_admin_access():
    client.post("/register", json={
        "username": "adminuser",
        "password": "adminpass",
        "role": "admin"
    })
    login = client.post("/login", json={
        "username": "adminuser",
        "password": "adminpass"
    })
    token = login.json()["access_token"]
    response = client.get("/admin", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    print("✅ test_admin_access passed")

# Test 6 — viewer cannot access admin panel
def test_viewer_blocked_from_admin():
    client.post("/register", json={
        "username": "vieweruser",
        "password": "viewerpass",
        "role": "viewer"
    })
    login = client.post("/login", json={
        "username": "vieweruser",
        "password": "viewerpass"
    })
    token = login.json()["access_token"]
    response = client.get("/admin", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 403
    print("✅ test_viewer_blocked_from_admin passed")