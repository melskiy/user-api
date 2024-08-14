from src.repository.interfaceses.repository_interface import RepositoryInterface
from src.factories.repository_factory import RepositoryFactory
from src.core.settings.settings import settings


def get_repository(session) -> RepositoryInterface:
    repo_type = settings.repository_type

    try:
        return RepositoryFactory.create(repo_type, session=session)
    except ValueError:
        raise ValueError("Invalid repository type")
