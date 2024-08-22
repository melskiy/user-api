from src.base.job_title.store.interfaceses.job_title_repository_interface import JobTitleRepositoryInterface
from src.base.job_title.store.redis.job_title_redis_database_factory import JobTitleRedisDatabaseFactory
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.db.redis.get_redis_connection_factory import GetRedisConnectionFactory
from src.core.db.redis.redis_settings import RedisSettings
from src.core.ioc import container


class JobTitleRedisDatabaseInitializer(Initialize):

    async def initialize(self):
        settings = container.resolve(RedisSettings)
        redis_connect = await GetRedisConnectionFactory()(settings)
        container.register(JobTitleRepositoryInterface, instance=lambda: JobTitleRedisDatabaseFactory()(redis_connect))
