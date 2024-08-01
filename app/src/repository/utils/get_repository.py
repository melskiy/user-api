from src.repository.interfaceses.repository_interface import RepositoryInterface
from src.repository.postgres_database import PostgresDatabase
from src.repository.redis_database import RedisDatabase
from src.factories.repository_factory import RepositoryFactory
from src.factories.repository_factory import RepositoryFactory
from src.core.settings import settings


RepositoryFactory.register("postgresql", PostgresDatabase)
RepositoryFactory.register("redis", RedisDatabase)


def get_repository() -> RepositoryInterface:
    repo_type = settings.repository_type

    if repo_type in settings.repository_list:
        return RepositoryFactory.create(repo_type)
    else:
        raise ValueError("Invalid repository type")
