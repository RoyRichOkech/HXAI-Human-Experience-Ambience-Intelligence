"""Memory model."""

from sqlalchemy import Column, String, DateTime, ForeignKey, Text, Enum
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from datetime import datetime
import uuid
import enum


class MemoryType(str, enum.Enum):
    """Types of memory."""

    SHORT_TERM = "short_term"
    LONG_TERM = "long_term"
    EPISODIC = "episodic"
    SEMANTIC = "semantic"
    PREFERENCE = "preference"
    HABIT = "habit"


class Memory(Base):
    """Memory model - stores user memories and information."""

    __tablename__ = "memories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    session_id = Column(UUID(as_uuid=True), ForeignKey("sessions.id"), nullable=True)
    memory_type = Column(Enum(MemoryType), default=MemoryType.SHORT_TERM)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    tags = Column(String, nullable=True)  # Comma-separated
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Memory(id={self.id}, user_id={self.user_id}, type={self.memory_type})>"
