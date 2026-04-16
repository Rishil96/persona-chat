import uuid
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text
from app.db.database import Base


class Conversation(Base):
    __tablename__ = 'conversations'
    id: Mapped[int] = mapped_column(primary_key=True)
    conversation_id: Mapped[str] = mapped_column(Text, unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
