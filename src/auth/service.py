from passlib.context import CryptContext
from src.database import SessionLocal
from src.models import User
from src.auth.schemas import UserCreate


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(email: str):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        return user
    finally:
        db.close()

def authenticate_user(email: str, password: str):
    user = get_user_by_email(email)
    if not user or not verify_password(password, user.password_hash):
        return False
    return user

def create_user(user_data: UserCreate):
    db = SessionLocal()
    try:    
        if get_user_by_email(user_data.email):
            raise ValueError("Email already registered")
        
        hashed_password = pwd_context.hash(user_data.password)
        
        db_user = User(
            email=user_data.email,
            password_hash=hashed_password,
            first_name=user_data.first_name,
            last_name=user_data.last_name
        )
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        db.close()
        return db_user
    finally:
        db.close()