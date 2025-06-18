import redis.asyncio as redis
from app.core.config import settings
import json
from typing import Any, Optional

class RedisClient:
    def __init__(self):
        self.redis_pool = None
    
    async def connect(self):
        """Initialize Redis connection pool"""
        self.redis_pool = redis.ConnectionPool.from_url(
            settings.REDIS_URL,
            encoding="utf-8",
            decode_responses=True,
            max_connections=20
        )
    
    async def get_client(self) -> redis.Redis:
        """Get Redis client instance"""
        if not self.redis_pool:
            await self.connect()
        return redis.Redis(connection_pool=self.redis_pool)
    
    async def set_cache(self, key: str, value: Any, expiry: int = 3600):
        """Set cache value with expiry"""
        client = await self.get_client()
        serialized_value = json.dumps(value, default=str)
        await client.setex(key, expiry, serialized_value)
    
    async def get_cache(self, key: str) -> Optional[Any]:
        """Get cache value"""
        client = await self.get_client()
        value = await client.get(key)
        if value:
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value
        return None
    
    async def delete_cache(self, key: str):
        """Delete cache key"""
        client = await self.get_client()
        await client.delete(key)
    
    async def check_health(self) -> bool:
        """Check Redis connection health"""
        try:
            client = await self.get_client()
            response = await client.ping()
            return response is True
        except Exception:
            return False
    
    async def close(self):
        """Close Redis connection"""
        if self.redis_pool:
            await self.redis_pool.disconnect()

# Global Redis client instance
redis_client = RedisClient() 