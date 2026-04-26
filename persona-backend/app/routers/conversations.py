from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.db.models import Conversation
from app.schemas.conversations import ConversationListItemSchema


router = APIRouter(prefix="/conversations", tags=["conversations"])


@router.post("/", response_model=ConversationListItemSchema, status_code=201)
def create_conversation(db: Annotated[Session, Depends(get_db)]):
    """
    Route to create a new conversation
    """
    new_conversation = Conversation()
    db.add(new_conversation)
    db.commit()
    db.refresh(new_conversation)
    return new_conversation
