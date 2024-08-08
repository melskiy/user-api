from fastapi import Depends

from src.repository.interfaceses.repository_interface import RepositoryInterface
from src.factories.repository_factory import RepositoryFactory
from src.core.settings import settings


def get_repository() -> RepositoryInterface:
    repo_type = settings.repository_type

    if repo_type in settings.repository_list:
        return RepositoryFactory.create(repo_type)
    raise ValueError("Invalid repository type")
