from src.base.user.store.interfaceses.user_repository_interface import UserRepositoryInterface


class DeleteUserService:
    def __init__(self, repo: UserRepositoryInterface):
        self.__repo = repo

    async def delete(self, id: str) -> None:
        await self.__repo.delete_item(id)
