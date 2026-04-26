from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.enums import Role


class MessageSchema(BaseModel):
    id: int = Field(..., description="Unique identifier for a single message")
    role: Role = Field(..., description="Message role, either user or assistant")
    content: str = Field(..., description="Message content")
    created_at: datetime = Field(..., description="Message creation date")


class ConversationSchema(BaseModel):
    conversation_id: str = Field(..., description="Unique conversation identifier")
    messages: List[MessageSchema] = Field(..., description="List of messages in this conversation")


class ConversationListItemSchema(BaseModel):
    conversation_id: str = Field(..., description="Conversation identifier")
    title: Optional[str] = Field(description="Conversation title", default=None)
