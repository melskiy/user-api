from src.base.user.models.user_base_model import UserBaseModel
from src.repository.interfaceses.repository_interface import RepositoryInterface


class CreateUserService:
    def __init__(self, repo: RepositoryInterface):
        self.__repo: RepositoryInterface = repo

    async def create(self, user: UserBaseModel) -> UserBaseModel:
        return await self.__repo.create_item(user)

