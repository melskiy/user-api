from src.repository.Interfaceses.RepositoryInterface import RepositoryInterface
from src.factories.RepositoryFactory import RepositoryFactory
from src.core.settings import settings

def getRepository( ) -> RepositoryInterface:
    repo_type = settings.repository_type
    
    if repo_type == 'memory':
        return RepositoryFactory.create(repo_type)
    elif repo_type in ['postgresql']:
        return RepositoryFactory.create(repo_type)
    else:
        raise ValueError("Invalid repository type")