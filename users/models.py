from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.orm import backref, relationship

from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    email = Column(String, unique=True)
    is_superuser = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    created = Column(DateTime)


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String)
    information = Column(Text)
    date_join = Column(DateTime)
    last_join = Column(DateTime)
    first_join = Column(DateTime)
    phone = Column(String)
    picture = Column(String)
    birthday = Column(String)
    town = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", backref=backref("profiles", uselist=False))
