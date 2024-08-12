from src.services.user.create_user import CreateUserService
from src.base.user.models.user_base_model import UserBaseModel


class CreateDataView:
    def __init__(self, service: CreateUserService):
        self.__service: CreateUserService = service

    async def __call__(self, user: UserBaseModel) -> UserBaseModel:
        return await self.__service.create(user)
