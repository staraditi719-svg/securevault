from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# This creates/connects to securevault.db file
DATABASE_URL = "sqlite:///./securevault.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ── User table ──
class UserModel(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)

# This creates the table in the database
def init_db():
    Base.metadata.create_all(bind=engine)

# Dependency — gives us a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ── Helper functions ──
def get_user(db, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()

def create_user(db, username: str, hashed_password: str, role: str):
    new_user = UserModel(
        username=username,
        hashed_password=hashed_password,
        role=role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user