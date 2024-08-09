from src.base.user.models.user_base_model import UserBaseModel
from src.repository.interfaceses.repository_interface import RepositoryInterface
from src.repository.utils.get_repository import get_repository


class CreateUserService:
    def __init__(self, repo: RepositoryInterface):
        self.repo: RepositoryInterface = repo

    async def create(self, user: UserBaseModel) -> UserBaseModel:
        return await self.repo.create_item(user)
