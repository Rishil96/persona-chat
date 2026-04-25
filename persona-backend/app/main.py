from dotenv import load_dotenv
from fastapi import FastAPI
from app.db.database import Base, get_engine

# Load environment variables
load_dotenv()

# Database setup
engine = get_engine()
Base.metadata.create_all(engine)

app = FastAPI(title="Persona")


@app.get("/health")
def health():
    return {"status": "ok"}
