import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


# Engine function
def get_engine():
    """
    Function to create and return a SQLAlchemy Engine object
    """
    url = os.environ.get("DATABASE_URL")
    return create_engine(url=url, connect_args={'check_same_thread': False})

# Session maker function
def get_session(engine):
    return sessionmaker(bind=engine, autoflush=False, autocommit=False)


# Base class for all ORM models
class Base(DeclarativeBase):
    pass
