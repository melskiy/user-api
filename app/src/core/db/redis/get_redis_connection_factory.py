import redis.asyncio as redis
from src.core.db.redis.get_redis_connection import get_redis_connection
from src.core.db.redis.redis_settings import RedisSettings


class GetRedisConnectionFactory:

    def __call__(self, settings: RedisSettings) -> redis:
        return get_redis_connection(
            settings=settings,
        )
