from src.repository.interfaceses.repository_interface import RepositoryInterface
from src.base.user.models.user_base_model import UserBaseModel


class UpdateUserService:
    def __init__(self, repo: RepositoryInterface):
        self.repo: RepositoryInterface = repo

    async def update(self, user: UserBaseModel) -> None:
        await self.repo.update_item(user)
