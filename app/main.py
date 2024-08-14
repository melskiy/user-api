import sys

from rodi import Container

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

    RepositoryFactory.register("postgresql", PostgresDatabase)
    RepositoryFactory.register("redis", RedisDatabase)

    RepositoryInitializer(container).initialize()
    ServiceInitializer(container).initialize()
    app = AppFactory.create(sys.argv[1], container=container).run(sys.argv[2:])

