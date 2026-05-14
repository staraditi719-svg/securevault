from pydantic import BaseModel

# This is what user sends when registering
class UserRegister(BaseModel):
    username: str
    password: str
    role: str  # "admin", "editor", or "viewer"

# This is what user sends when logging in
class UserLogin(BaseModel):
    username: str
    password: str

# This is the token we send back after login
class Token(BaseModel):
    access_token: str
    token_type: str