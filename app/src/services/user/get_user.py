from src.repository.interfaceses.repository_interface import RepositoryInterface
from src.base.user.models.user_base_model import UserBaseModel
from src.repository.utils.get_repository import get_repository


class GetUserService:
    def __init__(self, repo: RepositoryInterface):
        self.repo: RepositoryInterface = repo

    async def get(self, id) -> UserBaseModel:
        return await self.repo.read_item(id)
