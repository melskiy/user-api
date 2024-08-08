import sys

from src.apps.console_app import ConsoleApp
from src.apps.web_app import WebApp
from src.factories.app_factory import AppFactory
from src.repository.postgres_database import PostgresDatabase
from src.repository.redis_database import RedisDatabase
from src.factories.repository_factory import RepositoryFactory

RepositoryFactory.register("postgresql", PostgresDatabase)
RepositoryFactory.register("redis", RedisDatabase)
AppFactory.register("web", WebApp)
AppFactory.register("console", ConsoleApp)

if __name__ == "__main__":
    app = AppFactory.create(sys.argv[1])
    app.run(sys.argv[2:])
