"""Session schemas."""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


class SessionCreate(BaseModel):
    """Session creation schema."""

    title: Optional[str] = None
    description: Optional[str] = None


class SessionUpdate(BaseModel):
    """Session update schema."""

    title: Optional[str] = None
    description: Optional[str] = None


class SessionResponse(BaseModel):
    """Session response schema."""

    id: UUID
    user_id: UUID
    title: Optional[str]
    description: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
