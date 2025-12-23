import redis.asyncio as redis
from app.core.config import settings

class RedisClient:
    def __init__(self):
        self._client: redis.Redis | None = None

    async def connect(self):
        self._client = redis.from_url(settings.REDIS_URL, encoding="utf-8", decode_responses=True)
        await self._client.ping()

    @property
    def client(self) -> redis.Redis:
        if self._client is None:
            raise RuntimeError("Redis is not connected")
        return self._client

    async def close(self):
        if self._client is not None:
            await self._client.close()
            self._client = None

redis_client = RedisClient()
