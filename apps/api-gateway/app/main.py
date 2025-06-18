from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.core.config import settings
from app.core.redis_client import redis_client
from app.middleware.logging import LoggingMiddleware
from app.routers.health import router as health_router

# Configure logging
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    # Startup
    logger.info("Starting Job Application Automation System API")
    
    # Initialize Redis connection
    try:
        await redis_client.connect()
        logger.info("Redis connection established")
    except Exception as e:
        logger.error(f"Redis connection failed: {e}")
    
    yield
    
    # Shutdown
    logger.info("Shutting down Job Application Automation System API")
    
    # Close Redis connection
    try:
        await redis_client.close()
        logger.info("Redis connection closed")
    except Exception as e:
        logger.error(f"Error closing Redis connection: {e}")

# Create FastAPI application with lifespan events
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Job Application Automation System API - AI-powered job discovery and application assistance",
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Add custom middleware
app.add_middleware(LoggingMiddleware)

# Include routers
app.include_router(health_router, prefix="/api/v1", tags=["health"])

# Root endpoint
@app.get("/", tags=["root"])
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Job Application Automation System API",
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "docs_url": "/docs" if settings.DEBUG else "Disabled in production",
        "health_check": "/api/v1/health"
    }

# Legacy health endpoint (redirect to new health check)
@app.get("/health", tags=["health"])
async def legacy_health_check():
    """Legacy health endpoint - redirects to comprehensive health check"""
    return {
        "status": "healthy", 
        "version": settings.VERSION,
        "note": "Use /api/v1/health for detailed health information"
    }

# Global exception handler for development
if settings.DEBUG:
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.error(f"Global exception: {exc}", exc_info=True)
        return {
            "error": "Internal server error",
            "detail": str(exc) if settings.DEBUG else "Contact support",
            "path": str(request.url.path)
        }
