import redis.asyncio as redis
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.base.job_title.services.job_title_service_initializer import JobTitleServiceInitializer
from src.base.job_title.store.job_title_store_initialize import JobTitleStoreInitializer
from src.base.user.events.user_event_initilizer import UserEventInitializer
from src.base.user.services.user_service_initializer import UserServiceInitializer
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
        store_type = settings.repository_type
        load_dotenv()
        store_initializers = {
            'postgresql': lambda: container.register(
                async_sessionmaker,
                instance=
                PostgresSettings()
            ),
            'redis': lambda: container.register(
                redis,
                instance=
                RedisSettings()
            )
        }

        store_initializers.get(store_type)()
        await UserStoreInitializer().initialize()
        await JobTitleStoreInitializer().initialize()
        await JobTitleServiceInitializer().initialize()
        await UserEventInitializer().initialize()
        await UserServiceInitializer().initialize()
