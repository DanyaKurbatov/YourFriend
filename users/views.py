from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import timedelta
from sqlalchemy.orm import Session
from db import get_db
from users.operations import authenticate_user, create_access_token, create_user
from users.schemas import UserCreate, Token

users_router = APIRouter(prefix="/users",
                         tags=["Users"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
ACCESS_TOKEN_EXPIRE_MINUTES = 30


@users_router.post("/token", response_model=Token)
async def login_for_access_token(db: Session = Depends(get_db),
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
def create_users(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user(db=db, user=user)
    except:
        raise HTTPException(status_code=400,
                            detail="User already exists")
