"""Context schemas."""

from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
from uuid import UUID


class ContextCreate(BaseModel):
    """Context creation schema."""

    device: Optional[str] = None
    location: Optional[str] = None
    current_goal: Optional[str] = None
    current_activity: Optional[str] = None
    emotional_state: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class ContextUpdate(BaseModel):
    """Context update schema."""

    device: Optional[str] = None
    location: Optional[str] = None
    current_goal: Optional[str] = None
    current_activity: Optional[str] = None
    emotional_state: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class ContextResponse(BaseModel):
    """Context response schema."""

    id: UUID
    user_id: UUID
    session_id: Optional[UUID]
    device: Optional[str]
    location: Optional[str]
    current_goal: Optional[str]
    current_activity: Optional[str]
    emotional_state: Optional[str]
    metadata: Optional[Dict[str, Any]]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
