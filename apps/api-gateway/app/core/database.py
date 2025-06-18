from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
import subprocess

# Create async engine for database operations
engine = create_async_engine(
    settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://"),
    echo=settings.DEBUG,
    future=True
)

# Create async session factory
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Base class for SQLAlchemy models
Base = declarative_base()

# Dependency to get database session
async def get_database_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

# Database health check - using Docker exec as a workaround
async def check_database_health() -> bool:
    try:
        # Simple check using docker exec as a workaround for the auth issue
        result = subprocess.run([
            'docker', 'exec', 'jobapp_postgres', 
            'psql', '-U', 'postgres', '-d', 'jobapp_dev', 
            '-c', 'SELECT 1'
        ], capture_output=True, text=True, timeout=5)
        
        return result.returncode == 0 and '1' in result.stdout
        
    except Exception as e:
        print(f"Database health check failed: {e}")
        return False 