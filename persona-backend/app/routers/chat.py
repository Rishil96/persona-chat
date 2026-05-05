from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.schemas.chat_schemas import ChatInput, ChatOutput
from app.services.chat_service import send_message


router = APIRouter(prefix="/conversations", tags=["chat"])


@router.post("/{conversation_id}/messages", response_model=ChatOutput, status_code=200)
def chat(conversation_id: str, chat_input: ChatInput, db: Annotated[Session, Depends(get_db)]):
    """
    Route to continue a conversation using an existing conversation ID.
    """
    ai_response = send_message(conversation_id=conversation_id,
                               user_message=chat_input.user_message,
                               model_name=chat_input.model_name,
                               db=db)
    return ChatOutput(
        conversation_id=conversation_id,
        ai_response=ai_response
    )
