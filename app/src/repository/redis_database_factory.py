from redis.asyncio import Redis

from src.repository.redis_database import RedisDatabase


class RedisDatabaseFactory:

    def __call__(self, session: Redis, ) -> RedisDatabase:
        return RedisDatabase(
            session=session,
        )
