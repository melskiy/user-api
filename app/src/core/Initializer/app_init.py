from dotenv import load_dotenv

from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.db.get_postgre_connection import get_postgres_connection
from src.core.db.get_redis_connection import get_redis_connection
from src.core.ioc import container
from src.core.settings.postgres_settings import PostgresSettings
from src.core.settings.redis_settings import RedisSettings
from src.core.settings.settings import Settings
from src.repository.postgres.postgres_database_factory import PostgresDatabaseFactory
from src.repository.redis.redis_database_factory import RedisDatabaseFactory


class AppInitializer(Initialize):

    async def initialize(self):
        settings = Settings(
            _env_file=".env",
            _env_file_encoding="utf-8",
        )
        load_dotenv()
        postgres_settings = PostgresSettings()
        redis_settings = RedisSettings()
        pg_connect = await get_postgres_connection(postgres_settings)
        redis_connect = await get_redis_connection(redis_settings)

        container.register(get_postgres_connection, lambda: pg_connect)
        container.register(get_redis_connection, lambda: redis_connect)

        container.register('postgresql', instance=PostgresDatabaseFactory()(pg_connect))
        container.register('redis', instance=RedisDatabaseFactory()(redis_connect))

        container.register(Settings, instance=settings)
