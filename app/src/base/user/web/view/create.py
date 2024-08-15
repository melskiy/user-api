from src.base.user.models.user_base_model import UserBaseModel
from src.services.user.create_user import CreateUserService


class CreateDataView:
    def __init__(self, service: CreateUserService):
        self.__service: CreateUserService = service

    async def __call__(self, user: UserBaseModel) -> None:
        await self.__service.create(user)
