from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str


class UserInDB(UserBase):
    hashed_password: str


class UserCreate(UserBase):
    password: str
    email: EmailStr
    name: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
