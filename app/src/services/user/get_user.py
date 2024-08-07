from src.repository.interfaceses.repository_interface import RepositoryInterface
from src.base.user.models.user_base_model import UserBaseModel


class GetUserService:
    async def get(self, repo: RepositoryInterface, id) -> UserBaseModel:
        return await repo.read_item(id)
