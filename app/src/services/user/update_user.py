from src.repository.interfaceses.repository_interface import RepositoryInterface
from src.base.user.models.user_base_model import UserBaseModel


class UpdateUserService:
    async def update(self, repo: RepositoryInterface, user: UserBaseModel) -> None:
        await repo.update_item(user)
