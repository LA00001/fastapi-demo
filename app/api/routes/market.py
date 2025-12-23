from fastapi import APIRouter
from app.integrations.fmp import fmp_client
from app.cache.redis_client import redis_client

router = APIRouter()

@router.get("/quote/{ticker}")
async def quote(ticker: str):
    key = f"quote:{ticker.upper()}"
    cached = await redis_client.client.get(key)
    if cached:
        return {"source": "cache", "data": cached}
    data = await fmp_client.quote(ticker)
    await redis_client.client.set(key, str(data), ex=60)
    return {"source": "api", "data": data}
