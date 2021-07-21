from sqlalchemy import Column, Integer, String, DateTime, Boolean
from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    email = Column(String, unique=True)
    name = Column(String)
    date_join = Column(DateTime)
    last_join = Column(DateTime)
    first_join = Column(DateTime)
    is_superuser = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    phone = Column(String)
    picture = Column(String)
    birthday = Column(String)
