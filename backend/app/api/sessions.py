"""Session endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.session import Session as SessionModel
from app.models.user import User
from app.schemas.session import SessionCreate, SessionUpdate, SessionResponse
from app.api.users import get_current_user
from typing import List

router = APIRouter()


@router.post("/", response_model=SessionResponse)
async def create_session(
    session_data: SessionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create a new session."""
    new_session = SessionModel(
        user_id=current_user.id,
        **session_data.dict(),
    )
    
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    
    return new_session


@router.get("/", response_model=List[SessionResponse])
async def list_sessions(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """List user sessions."""
    sessions = db.query(SessionModel).filter(
        SessionModel.user_id == current_user.id
    ).offset(skip).limit(limit).all()
    
    return sessions


@router.get("/{session_id}", response_model=SessionResponse)
async def get_session(
    session_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get a specific session."""
    session = db.query(SessionModel).filter(
        SessionModel.id == session_id,
        SessionModel.user_id == current_user.id,
    ).first()
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found",
        )
    
    return session


@router.put("/{session_id}", response_model=SessionResponse)
async def update_session(
    session_id: str,
    session_data: SessionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Update a session."""
    session = db.query(SessionModel).filter(
        SessionModel.id == session_id,
        SessionModel.user_id == current_user.id,
    ).first()
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found",
        )
    
    for key, value in session_data.dict(exclude_unset=True).items():
        setattr(session, key, value)
    
    db.commit()
    db.refresh(session)
    
    return session


@router.delete("/{session_id}")
async def delete_session(
    session_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Delete a session."""
    session = db.query(SessionModel).filter(
        SessionModel.id == session_id,
        SessionModel.user_id == current_user.id,
    ).first()
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found",
        )
    
    db.delete(session)
    db.commit()
    
    return {"message": "Session deleted"}
