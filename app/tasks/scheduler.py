import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from app.cache.redis_client import redis_client

logger = logging.getLogger("scheduler")
scheduler = AsyncIOScheduler(timezone="UTC")

async def heartbeat_job():
    await redis_client.client.set("heartbeat", "ok")
    logger.info("heartbeat updated")

def register_jobs():
    scheduler.add_job(heartbeat_job, IntervalTrigger(seconds=60), id="heartbeat", replace_existing=True)

register_jobs()
