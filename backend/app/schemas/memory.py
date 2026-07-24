"""Memory schemas."""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID
from app.models.memory import MemoryType


class MemoryCreate(BaseModel):
    """Memory creation schema."""

    title: str
    content: str
    memory_type: MemoryType = MemoryType.SHORT_TERM
    tags: Optional[str] = None


class MemoryUpdate(BaseModel):
    """Memory update schema."""

    title: Optional[str] = None
    content: Optional[str] = None
    memory_type: Optional[MemoryType] = None
    tags: Optional[str] = None


class MemoryResponse(BaseModel):
    """Memory response schema."""

    id: UUID
    user_id: UUID
    session_id: Optional[UUID]
    title: str
    content: str
    memory_type: MemoryType
    tags: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
