from redis.asyncio import Redis

from src.base.user.store.redis.user_redis_database import UserRedisDatabase


class UserRedisDatabaseFactory:

    def __call__(self, session: Redis, ) -> UserRedisDatabase:
        return UserRedisDatabase(
            session=session,
        )
