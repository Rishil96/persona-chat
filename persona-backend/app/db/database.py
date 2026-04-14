import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(url=DATABASE_URL, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


# Base class for all ORM models
class Base(DeclarativeBase):
    pass
