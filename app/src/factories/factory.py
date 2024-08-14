from typing import Type, TypeVar, Dict

T = TypeVar('T')


class Factory:
    _creators: Dict[str, Type[T]] = {}

    @classmethod
    def register(cls, key: str, creator: Type[T]):
        cls._creators[key] = creator

    @classmethod
    def create(cls, key: str, **kwargs) -> T:
        creator = cls._creators.get(key)
        if not creator:
            raise ValueError(f"Тип репозитория '{key}' не зарегистрирован")
        return creator(**kwargs)
