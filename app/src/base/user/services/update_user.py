from src.base.user.store.interfaceses.repository_interface import UserRepositoryInterface
from src.base.user.models.user_base_model import UserBaseModel


class UpdateUserService:
    def __init__(self, repo: UserRepositoryInterface):
        self.__repo = repo

    async def update(self, user: UserBaseModel) -> None:
        await self.__repo.update_item(user)
