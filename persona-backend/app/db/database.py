import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


# Variables for singleton instantiation of engine and sessionmaker
engine = None
SessionLocal = None

# Engine function
def get_engine():
    """
    Function to create and return a SQLAlchemy Engine object
    """
    global engine
    if engine:
        return engine
    url = os.environ.get("DATABASE_URL", "sqlite:///./persona.db")
    engine = create_engine(url=url, connect_args={'check_same_thread': False})
    return engine

# Session maker function
def get_session():
    global engine, SessionLocal
    if SessionLocal:
        return SessionLocal
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    return SessionLocal


# Base class for all ORM models
class Base(DeclarativeBase):
    pass
