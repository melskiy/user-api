import sys

from rodi import Container
from fastapi import APIRouter

from src.apps.console_app import ConsoleApp
from src.apps.web_app import WebApp
from src.core.Initializer.repository_init import RepositoryInitializer
from src.core.Initializer.service_init import ServiceInitializer
from src.core.Initializer.web_init import WebInitializer
from src.core.Initializer.app import app

from src.factories.app_factory import AppFactory
from src.repository.postgres_database import PostgresDatabase
from src.repository.redis_database import RedisDatabase
from src.factories.repository_factory import RepositoryFactory

RepositoryFactory.register("postgresql", PostgresDatabase)
RepositoryFactory.register("redis", RedisDatabase)
AppFactory.register("web", WebApp)
AppFactory.register("console", ConsoleApp)


if __name__ == "__main__":
    container = Container()
    RepositoryInitializer(container).initialize()
    ServiceInitializer(container).initialize()
    AppFactory.create(sys.argv[1]).run(sys.argv[2:])
