"""Memory endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.memory import Memory
from app.models.user import User
from app.schemas.memory import MemoryCreate, MemoryUpdate, MemoryResponse
from app.api.users import get_current_user
from typing import List

router = APIRouter()


@router.post("/", response_model=MemoryResponse)
async def create_memory(
    memory_data: MemoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create a new memory."""
    new_memory = Memory(
        user_id=current_user.id,
        **memory_data.dict(),
    )
    
    db.add(new_memory)
    db.commit()
    db.refresh(new_memory)
    
    return new_memory


@router.get("/", response_model=List[MemoryResponse])
async def list_memories(
    memory_type: str = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """List user memories."""
    query = db.query(Memory).filter(Memory.user_id == current_user.id)
    
    if memory_type:
        query = query.filter(Memory.memory_type == memory_type)
    
    memories = query.offset(skip).limit(limit).all()
    return memories


@router.get("/{memory_id}", response_model=MemoryResponse)
async def get_memory(
    memory_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get a specific memory."""
    memory = db.query(Memory).filter(
        Memory.id == memory_id,
        Memory.user_id == current_user.id,
    ).first()
    
    if not memory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Memory not found",
        )
    
    return memory


@router.put("/{memory_id}", response_model=MemoryResponse)
async def update_memory(
    memory_id: str,
    memory_data: MemoryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Update a memory."""
    memory = db.query(Memory).filter(
        Memory.id == memory_id,
        Memory.user_id == current_user.id,
    ).first()
    
    if not memory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Memory not found",
        )
    
    for key, value in memory_data.dict(exclude_unset=True).items():
        setattr(memory, key, value)
    
    db.commit()
    db.refresh(memory)
    
    return memory


@router.delete("/{memory_id}")
async def delete_memory(
    memory_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Delete a memory."""
    memory = db.query(Memory).filter(
        Memory.id == memory_id,
        Memory.user_id == current_user.id,
    ).first()
    
    if not memory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Memory not found",
        )
    
    db.delete(memory)
    db.commit()
    
    return {"message": "Memory deleted"}
