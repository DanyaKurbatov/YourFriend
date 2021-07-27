from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from sqlalchemy.orm import Session
from db import get_db
from users.operations import authenticate_user, create_access_token, \
    create_user, get_users, get_user_by_id, delete_user_by_id
from users.schemas import UserCreate, Token
from config import ACCESS_TOKEN_EXPIRE_MINUTES
from users.users import get_current_active_user

users_router = APIRouter(prefix="/users",
                         tags=["Users"])


@users_router.post("/login", response_model=Token)
async def login(db: Session = Depends(get_db),
                form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@users_router.post('/create', response_model=UserCreate)
async def create_users(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user(db=db, user=user)
    except:
        raise HTTPException(status_code=400,
                            detail="User already exists")


@users_router.get('/', dependencies=[Depends(get_current_active_user)])
async def get_users_all(db: Session = Depends(get_db)):
    try:
        return get_users(db)
    except:
        raise HTTPException(status_code=500,
                            detail="INTERNAL_SERVER_ERROR")


@users_router.get('/{id}', dependencies=[Depends(get_current_active_user)])
async def get_user_by(id: int,
                      db: Session = Depends(get_db)):
    user = get_user_by_id(db, id)
    if user is None:
        raise HTTPException(status_code=404,
                            detail="User not found")
    return user


@users_router.delete('/{id}', dependencies=[Depends(get_current_active_user)])
async def delete_user_by(id: int,
                         db: Session = Depends(get_db)):
    if get_user_by_id(db, id) is None:
        raise HTTPException(status_code=404,
                            detail="User not found")
    user = delete_user_by_id(db, id)
    return user
