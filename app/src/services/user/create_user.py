from src.repository.interfaceses.repository_interface import RepositoryInterface
from src.base.user.models.user_base_model import UserBaseModel


class CreateUserService:
    async def create(self, repo: RepositoryInterface, user: UserBaseModel) -> UserBaseModel:
        return await repo.create_item(user)
