from datetime import datetime
from pydantic import BaseModel, Field
from app.enums import Role


class MessageSchema(BaseModel):
    id: int = Field(..., description="Unique identifier for a single message")
    role: Role = Field(..., description="Message role, either user or assistant")
    content: str = Field(..., description="Message content")
    created_at: datetime = Field(..., description="Message creation date")
