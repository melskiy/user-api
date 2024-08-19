import redis.asyncio as Redis
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.base.job_title.store.job_title_store_initialize import JobTitleStoreInitializer
from src.base.user.store.user_store_initialize import UserStoreInitializer
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.db.postgres.get_postgre_connection_factory import GetPostgresConnectionFactory
from src.core.db.redis.get_redis_connection_factory import GetRedisConnectionFactory
from src.core.ioc import container
from src.core.settings.postgres_settings import PostgresSettings
from src.core.settings.redis_settings import RedisSettings
from src.core.settings.settings import Settings


class AppInitializer(Initialize):

    async def initialize(self):
        settings = Settings(
            _env_file=".env",
            _env_file_encoding="utf-8",
        )
        container.register(Settings, instance=settings)

        load_dotenv()

        postgres_settings = PostgresSettings()
        redis_settings = RedisSettings()

        container.register(async_sessionmaker, instance=GetPostgresConnectionFactory()(postgres_settings))
        container.register(Redis, instance=GetRedisConnectionFactory()(redis_settings))

        await JobTitleStoreInitializer().initialize()
        await UserStoreInitializer().initialize()
