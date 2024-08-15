from src.base.job_title.store.postgres.job_title_postgres_database_initialize import JobTitlePostgresDatabaseInitializer
from src.base.job_title.store.postgres.postgres_database import JobTitlePostgresDatabase
from src.base.job_title.store.redis.job_title_redis_database_Initializer import JobTitleRedisDatabaseInitializer
from src.base.job_title.store.redis.redis_database import JobTitleRedisDatabase
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container
from src.core.settings.settings import Settings


class JobTitleStoreInitializer(Initialize):

    async def initialize(self):
        settings = container.resolve(Settings)
        if settings.repository_type == 'postgresql':
            await JobTitlePostgresDatabaseInitializer().initialize()
            container.register(settings.repository_type, instance=container.resolve(JobTitlePostgresDatabase))
        if settings.repository_type == 'redis':
            await JobTitleRedisDatabaseInitializer().initialize()
            container.register(settings.repository_type, instance=container.resolve(JobTitleRedisDatabase))
