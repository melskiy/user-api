from src.base.user.store.postgres.user_postgres_database import UserPostgresDatabase
from src.base.user.store.postgres.user_postgres_database_Initializer import UserPostgresDatabaseInitializer
from src.base.user.store.redis.user_redis_database import UserRedisDatabase
from src.base.user.store.redis.user_redis_database_Initializer import UserRedisDatabaseInitializer
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container

from src.core.settings.settings import Settings


class UserStoreInitializer(Initialize):

    async def initialize(self):
        settings = container.resolve(Settings)
        if settings.repository_type == 'postgresql':
            UserPostgresDatabaseInitializer()
            container.register(settings.repository_type, container.resolve(UserPostgresDatabase))
        if settings.repository_type == 'redis':
            UserRedisDatabaseInitializer()
            container.register(settings.repository_type, container.resolve(UserRedisDatabase))
