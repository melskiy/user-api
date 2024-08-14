import sys
from typing import Type

from redis.asyncio import Redis

from fastapi import APIRouter
from rodi import Container
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.apps.console_app import ConsoleApp
from src.apps.web_app import WebApp
from src.core.Initializer.postgress_init import PostgresInitializer
from src.core.Initializer.redis_init import RedisInitializer
from src.core.Initializer.repository_init import RepositoryInitializer
from src.core.Initializer.service_init import ServiceInitializer
from src.core.Initializer.web_init import WebInitializer
from src.core.settings.settings import Settings
from src.factories.factory import Factory

from src.repository.postgres_database import PostgresDatabase
from src.repository.redis_database import RedisDatabase

if __name__ == "__main__":
    router = APIRouter()
    container = Container()
    container.register(APIRouter, instance=router)
    settings = Settings(
        _env_file=".env",
        _env_file_encoding="utf-8",
    )

    RedisInitializer(container).initialize()
    PostgresInitializer(container).initialize()

    Factory.register("web", WebApp)
    Factory.register("console", ConsoleApp)

    Factory.register("postgresql", PostgresDatabase)
    Factory.register("redis", RedisDatabase)

    Factory.register("postgresql" + "session", container.resolve(Type[async_sessionmaker]))
    Factory.register("redis" + "session", container.resolve(Type[Redis]))

    RepositoryInitializer(container, settings).initialize()
    ServiceInitializer(container).initialize()
    WebInitializer(container).initialize()

    app = Factory.create(sys.argv[1], container=container, settings=settings).run(sys.argv[2:])
