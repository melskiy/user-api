from src.base.job_title.store import redis
from src.base.user.store.redis.user_redis_database import UserRedisDatabase
from src.base.user.store.redis.user_redis_database_factory import UserRedisDatabaseFactory
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container


class UserRedisDatabaseInitializer(Initialize):

    async def initialize(self):
        redis_connect = container.resolve(redis)
        container.register(UserRedisDatabase, instance=UserRedisDatabaseFactory()(redis_connect))
