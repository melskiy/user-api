import redis.asyncio as redis

from src.core.settings.redis_settings import RedisSettings


async def get_redis_connection(settings: RedisSettings):
    return redis.Redis(
        host=settings.redis_host, port=settings.redis_port, decode_responses=True
    )
