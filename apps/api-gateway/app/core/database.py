"""
Database Configuration and Session Management
"""

import asyncio
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import logging

from app.core.config import settings
from app.models import Base

logger = logging.getLogger(__name__)

# Create async engine
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_pre_ping=True,
    pool_recycle=300,
    pool_size=10,
    max_overflow=20,
)

# Create async session factory
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency to get database session"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception as e:
            logger.error(f"Database session error: {e}")
            await session.rollback()
            raise
        finally:
            await session.close()


async def init_db() -> None:
    """Initialize database with tables"""
    try:
        async with engine.begin() as conn:
            # Run the migration file instead of create_all
            migration_file = "migrations/001_initial_schema.sql"
            try:
                await run_migration(migration_file)
                logger.info("Database migration executed successfully")
            except FileNotFoundError:
                # Fallback to SQLAlchemy create_all if migration file not found
                await conn.run_sync(Base.metadata.create_all)
                logger.info("Database tables created successfully (fallback)")
            
            # Verify pgvector extension
            result = await conn.execute(text("SELECT * FROM pg_extension WHERE extname = 'pgvector'"))
            if result.fetchone():
                logger.info("pgvector extension is available")
            else:
                logger.warning("pgvector extension not found - vector search will not work")
                
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")
        raise


async def run_migration(migration_file: str) -> None:
    """Run a specific migration file"""
    try:
        with open(migration_file, 'r') as f:
            migration_sql = f.read()
        
        async with engine.begin() as conn:
            await conn.execute(text(migration_sql))
            logger.info(f"Migration {migration_file} executed successfully")
            
    except Exception as e:
        logger.error(f"Migration {migration_file} failed: {e}")
        raise


async def check_db_health() -> dict:
    """Check database health and connectivity"""
    try:
        async with AsyncSessionLocal() as session:
            # Test basic connectivity
            result = await session.execute(text("SELECT 1"))
            result.fetchone()
            
            # Check if tables exist
            result = await session.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                AND table_name IN ('users', 'job_postings', 'applications')
            """))
            tables = [row[0] for row in result.fetchall()]
            
            # Check pgvector extension
            result = await session.execute(text("SELECT * FROM pg_extension WHERE extname = 'pgvector'"))
            pgvector_available = result.fetchone() is not None
            
            return {
                "status": "healthy",
                "tables_exist": len(tables) >= 3,
                "pgvector_available": pgvector_available,
                "tables_found": tables
            }
            
    except Exception as e:
        logger.error(f"Database health check failed: {e}")
        return {
            "status": "unhealthy",
            "error": str(e),
            "tables_exist": False,
            "pgvector_available": False,
            "tables_found": []
        }


async def close_db() -> None:
    """Close database connections"""
    await engine.dispose()
    logger.info("Database connections closed") 