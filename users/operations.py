from typing import Optional
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from users import models
from users.schemas import UserCreate
from jose import jwt
from config import pwd_context, SECRET_KEY, ALGORITHM


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username,
                          email=user.email,
                          password=hashed_password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)


def get_user(db: Session, username: str):
    return db.query(models.User).filter(
        models.User.username == username).first()


def get_user_by_id(db: Session, id: int):
    return db.query(models.User).filter(
        models.User.id == id).first()


def delete_user_by_id(db: Session, id: int):
    db.query(models.User).filter(
        models.User.id == id).delete()
    db.commit()


def get_users(db: Session):
    return db.query(models.User).all()


def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
