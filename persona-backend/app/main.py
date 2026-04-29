import logging
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from app.db.database import Base, get_engine, get_session
from app.logger import setup_logger
from app.routers.conversations import router as conversation_router
from app.constants import LOGGER_NAME, DEFAULT_LOGGER

# Load environment variables
load_dotenv()

# Setup singleton logger
setup_logger()
logger = logging.getLogger(os.getenv(LOGGER_NAME, DEFAULT_LOGGER))

# Database setup
engine = get_engine()
SessionLocal = get_session()
Base.metadata.create_all(engine)

app = FastAPI(title="Persona")
app.include_router(conversation_router)


@app.get("/health")
def health():
    return {"status": "ok"}
