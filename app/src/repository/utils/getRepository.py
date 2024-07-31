from src.repository.Interfaceses.RepositoryInterface import RepositoryInterface
from src.factories.RepositoryFactory import RepositoryFactory
from src.core.settings import settings
from src.repository.PostgresDatabase import PostgresDatabase
from src.repository.RedisDatabase import RedisDatabase
from src.factories.RepositoryFactory import RepositoryFactory

RepositoryFactory.register('postgresql', PostgresDatabase)
RepositoryFactory.register('redis', RedisDatabase)

def getRepository( ) -> RepositoryInterface:
    repo_type = settings.repository_type

    if repo_type in ['postgresql','redis']:
        return RepositoryFactory.create(repo_type)
    else:
        raise ValueError("Invalid repository type")