from src.repository.Interfaceses.RepositoryInterface import RepositoryInterface
from src.factories.RepositoryFactory import RepositoryFactory
from src.core.settings import settings
from src.repository.InMemoryDatabase import InMemoryDatabase
from src.repository.PostgresDatabase import PostgresDatabase
from src.factories.RepositoryFactory import RepositoryFactory

RepositoryFactory.register('memory', InMemoryDatabase)
RepositoryFactory.register('postgresql', PostgresDatabase)


def getRepository( ) -> RepositoryInterface:
    repo_type = settings.repository_type
    
    if repo_type == 'memory':
        return RepositoryFactory.create(repo_type)
    elif repo_type in ['postgresql']:
        return RepositoryFactory.create(repo_type)
    else:
        raise ValueError("Invalid repository type")