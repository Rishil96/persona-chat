from pydantic import BaseModel, Field


class ChatInput(BaseModel):
    user_message: str = Field(description="User message")
    model_name: str = Field(description="Model Name")


class ChatOutput(BaseModel):
    conversation_id: str = Field(description="Conversation ID")
    ai_response: str = Field(description="AI response")
