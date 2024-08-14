from src.factories.factory import Factory
from src.repository.interfaceses.repository_interface import RepositoryInterface


def get_repository(session, repo_type) -> RepositoryInterface:
    try:
        return Factory.create(repo_type, session=session)
    except ValueError:
        raise ValueError("Invalid repository type")
