import logging
from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base
from app.cache.redis_client import redis_client
from app.api.router import api_router
from app.tasks.scheduler import scheduler
from app.integrations.http_client import http_pool

def create_app() -> FastAPI:
    logging.basicConfig(level=getattr(logging, settings.LOG_LEVEL, logging.INFO))
    app = FastAPI(title=settings.APP_NAME, version="0.1.0")
    app.include_router(api_router, prefix="/api/v1")

    @app.on_event("startup")
    async def startup():
        await redis_client.connect()
        scheduler.start()
        if settings.AUTO_CREATE_DB:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)

    @app.on_event("shutdown")
    async def shutdown():
        scheduler.shutdown(wait=False)
        await redis_client.close()
        await http_pool.close()
        await engine.dispose()

    return app

app = create_app()
