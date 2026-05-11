# Fake database using a dictionary for now
# Later we will replace this with a real SQLite database

fake_db = {}

def get_user(username: str):
    if username in fake_db:
        return fake_db[username]
    return None

def create_user(username: str, hashed_password: str, role: str):
    fake_db[username] = {
        "username": username,
        "hashed_password": hashed_password,
        "role": role
    }