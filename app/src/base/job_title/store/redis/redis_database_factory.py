from redis.asyncio import Redis

from src.base.job_title.store.redis.redis_database import RedisDatabase


class RedisDatabaseFactory:

    def __call__(self, session: Redis, ) -> RedisDatabase:
        return RedisDatabase(
            session=session,
        )
