from src.repository.interfaceses.repository_interface import RepositoryInterface
from src.base.user.models.user_base_model import UserBaseModel


class GetUserService:
    def __init__(self, repo: RepositoryInterface):
        self.__repo: RepositoryInterface = repo

    async def get(self, id) -> UserBaseModel:
        return await self.__repo.read_item(id)
