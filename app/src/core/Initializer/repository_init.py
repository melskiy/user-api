from typing import Type
import redis.asyncio as redis

from rodi import Container
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.settings.settings import settings
from src.repository.utils.get_repository import get_repository


class RepositoryInitializer(Initialize):

    def __init__(self, __container: Container):
        self.__container = __container

    def initialize(self):
        container = self.__container
        sessions = {
            'postgresql': container.resolve(Type[async_sessionmaker]),
            'redis': container.resolve(redis.Redis)
        }
        container.register(get_repository, instance=get_repository(sessions[settings.repository_type]))
