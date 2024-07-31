from typing import Type
from src.repository.Interfaceses.RepositoryInterface import RepositoryInterface

class RepositoryFactory:
    _creators = {}

    @classmethod
    def register(cls, key: str, creator: Type[RepositoryInterface]):
        cls._creators[key] = creator

    @classmethod
    def create(cls, key: str, **kwargs) -> RepositoryInterface:
        creator = cls._creators.get(key)
        if not creator:
            raise ValueError(f"Repository type '{key}' is not registered")
        return creator(**kwargs)
