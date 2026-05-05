import uuid
from datetime import datetime, UTC
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Text, ForeignKey, DateTime, Enum, String
from app.db.database import Base
from app.enums import Role


# Conversation table schema
class Conversation(Base):
    __tablename__ = 'conversations'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=True)
    conversation_id: Mapped[str] = mapped_column(Text, unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    messages = relationship("Message", cascade="all, delete-orphan")


# Message table schema
class Message(Base):
    __tablename__ = 'messages'
    id: Mapped[int] = mapped_column(primary_key=True)
    conversation_id: Mapped[int] = mapped_column(ForeignKey('conversations.id'), nullable=False)
    role: Mapped[Role] = mapped_column(Enum(Role), nullable=False)
    model: Mapped[str] = mapped_column(String, nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=lambda: datetime.now(UTC))
