from dotenv import load_dotenv
from fastapi import FastAPI
from app.db.database import Base, get_engine, get_session
from app.routers.conversations import router as conversation_router
from app.routers.chat import router as chat_router

# Load environment variables
load_dotenv()

# Database setup
engine = get_engine()
SessionLocal = get_session()
Base.metadata.create_all(engine)

app = FastAPI(title="Persona")
app.include_router(conversation_router)
app.include_router(chat_router)


@app.get("/health")
def health():
    return {"status": "ok"}
