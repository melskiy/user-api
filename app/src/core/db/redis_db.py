import redis.asyncio as redis
from src.core.settings import settings
from redis.asyncio.client import Redis


def sessional() -> Redis:
    repo = redis.Redis(
        host=settings.redis_host, port=settings.redis_port, decode_responses=True
    )
    return repo
