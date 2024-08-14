from src.base.user.models.user_base_model import UserBaseModel
from src.events.event_manger import EventManager
from src.repository.interfaceses.repository_interface import RepositoryInterface


class CreateUserService:
    def __init__(self, repo: RepositoryInterface, manager: EventManager):
        self.__repo: RepositoryInterface = repo
        self.__manager = manager

    async def create(self, user: UserBaseModel) -> None:
        await self.__repo.create_item(user)
        await self.__manager.notify()
