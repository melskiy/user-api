from src.base.user.events.user_created_event import UserCreatedEvent
from src.base.user.models.user_base_model import UserBaseModel
from src.events.event_manger import EventManager
from src.base.user.store.interfaceses.user_repository_interface import UserRepositoryInterface


class CreateUserService:
    def __init__(self, repo: UserRepositoryInterface, event_manager: EventManager):
        self.__repo = repo
        self.__event_manager = event_manager

    async def create(self, user: UserBaseModel) -> None:
        await self.__repo.create_item(user)
        event = UserCreatedEvent()
        await self.__event_manager.notify(event)
