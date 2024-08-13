from typing import Type

from dotenv import load_dotenv
from redis.asyncio import Redis
from rodi import Container
import redis.asyncio as redis

from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.settings.redis_settings import RedisSettings


class RedisInitializer(Initialize):

    def __init__(self, __container: Container):
        self.__container = __container

    def initialize(self):
        container = self.__container
        load_dotenv('src/core/settings/.env')
        redis_settings = RedisSettings()

        session = redis.Redis(
            host=redis_settings.redis_host, port=redis_settings.redis_port, decode_responses=True
        )
        container.register(Redis, instance=session)



