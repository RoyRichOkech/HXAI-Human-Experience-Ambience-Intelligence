"""Context model."""

from sqlalchemy import Column, String, DateTime, ForeignKey, Text, JSON
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from datetime import datetime
import uuid


class Context(Base):
    """Context model - stores user context and environment state."""

    __tablename__ = "contexts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    session_id = Column(UUID(as_uuid=True), ForeignKey("sessions.id"), nullable=True)
    device = Column(String, nullable=True)  # e.g., "laptop", "phone", "tablet"
    location = Column(String, nullable=True)
    current_goal = Column(Text, nullable=True)
    current_activity = Column(String, nullable=True)
    emotional_state = Column(String, nullable=True)
    metadata = Column(JSON, default=dict)  # Additional context data
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Context(id={self.id}, user_id={self.user_id}, device={self.device})>"
