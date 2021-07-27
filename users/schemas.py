from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str


class User(UserBase):
    id: Optional[int] = None
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    is_superuser: Optional[bool] = None
    is_active: Optional[bool] = None


class UserInDB(UserBase):
    hashed_password: str


class UserCreate(UserBase):
    password: str
    email: EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
