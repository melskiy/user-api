import sys
from typing import Type

import redis.asyncio as redis
from rodi import Container
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.apps.console_app import ConsoleApp
from src.apps.web_app import WebApp
from src.core.Initializer.postgress_init import PostgresInitializer
from src.core.Initializer.redis_init import RedisInitializer
from src.core.Initializer.repository_init import RepositoryInitializer
from src.core.Initializer.service_init import ServiceInitializer

from src.factories.app_factory import AppFactory
from src.factories.repository_factory import RepositoryFactory
from src.repository.postgres_database import PostgresDatabase
from src.repository.redis_database import RedisDatabase

if __name__ == "__main__":

    container = Container()
    RedisInitializer(container).initialize()
    PostgresInitializer(container).initialize()
    AppFactory.register("web", WebApp)
    AppFactory.register("console", ConsoleApp)

    RepositoryInitializer(container).initialize()
    ServiceInitializer(container).initialize()
    AppFactory.create(sys.argv[1]).run(sys.argv[2:], container=container)
