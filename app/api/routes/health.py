from fastapi import APIRouter
from sqlalchemy import text
from app.db.session import engine
from app.cache.redis_client import redis_client

router = APIRouter()

@router.get("/health")
async def health():
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    await redis_client.client.ping()
    return {"status": "ok"}
