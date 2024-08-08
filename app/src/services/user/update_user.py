from src.repository.interfaceses.repository_interface import RepositoryInterface
from src.base.user.models.user_base_model import UserBaseModel
from src.repository.utils.get_repository import get_repository


class UpdateUserService:
    def __init__(self):
        self.repo: RepositoryInterface = get_repository()

    async def update(self, user: UserBaseModel) -> None:
        await self.repo.update_item(user)
