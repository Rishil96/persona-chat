from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import Base, get_engine, get_session
from app.logger import get_logger
from app.routers.conversations import router as conversation_router
from app.routers.chat import router as chat_router

# Load environment variables
load_dotenv()

# Database setup
engine = get_engine()
SessionLocal = get_session()
Base.metadata.create_all(engine)

# Logger setup
logger = get_logger()

# App setup
app = FastAPI(title="Persona")
app.include_router(conversation_router)
app.include_router(chat_router)

# Setup Middleware
origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get("/health")
def health():
    logger.info("Persona Chat is running.")
    return {"status": "ok"}
