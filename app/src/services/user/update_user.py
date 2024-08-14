from src.repository.interfaceses.repository_interface import RepositoryInterface
from src.base.user.models.user_base_model import UserBaseModel


class UpdateUserService:
    def __init__(self, repo: RepositoryInterface):
        self.__repo: RepositoryInterface = repo

    async def update(self, user: UserBaseModel) -> None:
        await self.__repo.update_item(user)
