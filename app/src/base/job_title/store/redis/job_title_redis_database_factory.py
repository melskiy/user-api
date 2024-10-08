from redis.asyncio import Redis

from src.base.job_title.store.redis.job_title_redis_database import JobTitleRedisDatabase


class JobTitleRedisDatabaseFactory:

    def __call__(self, session: Redis, ) -> JobTitleRedisDatabase:
        return JobTitleRedisDatabase(
            session=session,
        )
