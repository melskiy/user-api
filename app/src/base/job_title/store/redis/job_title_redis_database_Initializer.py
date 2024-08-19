import redis.asyncio as redis
from src.base.job_title.store.redis.redis_database import JobTitleRedisDatabase
from src.base.job_title.store.redis.redis_database_factory import JobTitleRedisDatabaseFactory
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container


class JobTitleRedisDatabaseInitializer(Initialize):

    async def initialize(self):
        redis_connect = await container.resolve(redis)
        container.register(JobTitleRedisDatabase, instance=JobTitleRedisDatabaseFactory()(redis_connect))
