"""Context endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.context import Context
from app.models.user import User
from app.schemas.context import ContextCreate, ContextUpdate, ContextResponse
from app.api.users import get_current_user

router = APIRouter()


@router.post("/", response_model=ContextResponse)
async def create_context(
    context_data: ContextCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create or update user context."""
    # Check if context exists for current session
    existing_context = db.query(Context).filter(
        Context.user_id == current_user.id
    ).first()
    
    if existing_context:
        # Update existing
        for key, value in context_data.dict(exclude_unset=True).items():
            setattr(existing_context, key, value)
        db.commit()
        db.refresh(existing_context)
        return existing_context
    
    # Create new
    new_context = Context(
        user_id=current_user.id,
        **context_data.dict(),
    )
    
    db.add(new_context)
    db.commit()
    db.refresh(new_context)
    
    return new_context


@router.get("/", response_model=ContextResponse)
async def get_context(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get user context."""
    context = db.query(Context).filter(
        Context.user_id == current_user.id
    ).first()
    
    if not context:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Context not found",
        )
    
    return context


@router.put("/", response_model=ContextResponse)
async def update_context(
    context_data: ContextUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Update user context."""
    context = db.query(Context).filter(
        Context.user_id == current_user.id
    ).first()
    
    if not context:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Context not found",
        )
    
    for key, value in context_data.dict(exclude_unset=True).items():
        setattr(context, key, value)
    
    db.commit()
    db.refresh(context)
    
    return context
