"""User schemas."""

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from uuid import UUID


class UserCreate(BaseModel):
    """User creation schema."""

    email: EmailStr
    username: str
    password: str
    full_name: Optional[str] = None


class UserLogin(BaseModel):
    """User login schema."""

    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """User response schema."""

    id: UUID
    email: str
    username: str
    full_name: Optional[str]
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    """Token response schema."""

    access_token: str
    token_type: str = "bearer"
    user: UserResponse
