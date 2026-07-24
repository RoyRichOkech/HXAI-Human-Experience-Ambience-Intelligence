"""Application lifecycle events."""

import logging

logger = logging.getLogger(__name__)


async def startup_event():
    """Startup event handler."""
    logger.info("Application startup")
    # Initialize connections, load models, etc.


async def shutdown_event():
    """Shutdown event handler."""
    logger.info("Application shutdown")
    # Close connections, cleanup, etc.
