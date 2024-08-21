import redis.asyncio as redis

from src.base.user.store.interfaceses.user_repository_interface import UserRepositoryInterface
from src.base.user.store.redis.user_redis_database_factory import UserRedisDatabaseFactory
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.db.redis.get_redis_connection_factory import GetRedisConnectionFactory
from src.core.ioc import container


class UserRedisDatabaseInitializer(Initialize):

    async def initialize(self):
        settings = container.resolve(redis)
        redis_connect = await GetRedisConnectionFactory()(settings)
        container.register(UserRepositoryInterface, instance=lambda: UserRedisDatabaseFactory()(redis_connect))

