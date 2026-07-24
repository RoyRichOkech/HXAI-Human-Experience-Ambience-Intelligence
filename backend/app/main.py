"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.core.config import settings
from app.core.database import engine, Base
from app.api import auth, users, memory, context, sessions
from app.core.events import startup_event, shutdown_event

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage app lifecycle."""
    # Startup
    logger.info("Starting HXAI Backend")
    Base.metadata.create_all(bind=engine)
    await startup_event()
    yield
    # Shutdown
    logger.info("Shutting down HXAI Backend")
    await shutdown_event()


app = FastAPI(
    title="HXAI API",
    description="Human Experience Ambient Intelligence API",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check
@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "version": "0.1.0"}


# Root endpoint
@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to HXAI - Human Experience Ambient Intelligence",
        "api_docs": "/docs",
        "version": "0.1.0",
    }


# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(memory.router, prefix="/api/memory", tags=["Memory"])
app.include_router(context.router, prefix="/api/context", tags=["Context"])
app.include_router(sessions.router, prefix="/api/sessions", tags=["Sessions"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
