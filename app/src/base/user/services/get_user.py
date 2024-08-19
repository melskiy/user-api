from src.base.user.store.interfaceses.repository_interface import UserRepositoryInterface
from src.base.user.models.user_base_model import UserBaseModel


class GetUserService:
    def __init__(self, repo: UserRepositoryInterface):
        self.__repo = repo

    async def get(self, id) -> UserBaseModel:
        return await self.__repo.read_item(id)
