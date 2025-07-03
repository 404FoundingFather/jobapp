from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import asyncio
from datetime import datetime

from app.core.config import settings
from app.core.database import check_db_health
from app.core.redis_client import redis_client

router = APIRouter()

class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    version: str
    environment: str
    services: Dict[str, Any]

class ServiceHealth(BaseModel):
    status: str
    response_time_ms: float
    details: Dict[str, Any] = {}

@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Comprehensive health check for all system components"""
    start_time = asyncio.get_event_loop().time()
    
    services = {}
    overall_status = "healthy"
    
    # Check Database
    try:
        db_start = asyncio.get_event_loop().time()
        db_health = await check_db_health()
        db_time = (asyncio.get_event_loop().time() - db_start) * 1000
        
        services["database"] = ServiceHealth(
            status=db_health["status"],
            response_time_ms=round(db_time, 2),
            details={
                "url": settings.DATABASE_URL.split("@")[1] if "@" in settings.DATABASE_URL else "hidden",
                "tables_exist": db_health["tables_exist"],
                "pgvector_available": db_health["pgvector_available"],
                "tables_found": db_health["tables_found"]
            }
        )
        
        if db_health["status"] != "healthy":
            overall_status = "degraded"
            
    except Exception as e:
        services["database"] = ServiceHealth(
            status="unhealthy",
            response_time_ms=0,
            details={"error": str(e)}
        )
        overall_status = "unhealthy"
    
    # Check Redis
    try:
        redis_start = asyncio.get_event_loop().time()
        redis_healthy = await redis_client.check_health()
        redis_time = (asyncio.get_event_loop().time() - redis_start) * 1000
        
        services["redis"] = ServiceHealth(
            status="healthy" if redis_healthy else "unhealthy",
            response_time_ms=round(redis_time, 2),
            details={"url": settings.REDIS_URL.split("@")[1] if "@" in settings.REDIS_URL else settings.REDIS_URL}
        )
        
        if not redis_healthy:
            overall_status = "degraded"
            
    except Exception as e:
        services["redis"] = ServiceHealth(
            status="unhealthy",
            response_time_ms=0,
            details={"error": str(e)}
        )
        overall_status = "unhealthy"
    
    # Check OpenAI API availability (basic check)
    try:
        openai_start = asyncio.get_event_loop().time()
        openai_configured = settings.OPENAI_API_KEY != "your-openai-api-key-here"
        openai_time = (asyncio.get_event_loop().time() - openai_start) * 1000
        
        services["openai"] = ServiceHealth(
            status="configured" if openai_configured else "not_configured",
            response_time_ms=round(openai_time, 2),
            details={"configured": openai_configured}
        )
        
        if not openai_configured:
            overall_status = "degraded"
            
    except Exception as e:
        services["openai"] = ServiceHealth(
            status="error",
            response_time_ms=0,
            details={"error": str(e)}
        )
    
    total_time = asyncio.get_event_loop().time() - start_time
    
    return HealthResponse(
        status=overall_status,
        timestamp=datetime.utcnow(),
        version=settings.VERSION,
        environment=settings.ENVIRONMENT,
        services=services
    )

@router.get("/health/ready")
async def readiness_check():
    """Kubernetes-style readiness check"""
    db_health = await check_db_health()
    redis_healthy = await redis_client.check_health()
    
    if db_health["status"] == "healthy" and redis_healthy:
        return {"status": "ready"}
    else:
        raise HTTPException(status_code=503, detail="Service not ready")

@router.get("/health/live")
async def liveness_check():
    """Kubernetes-style liveness check"""
    return {"status": "alive", "timestamp": datetime.utcnow()} 