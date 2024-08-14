from src.repository.interfaceses.repository_interface import RepositoryInterface


class DeleteUserService:
    def __init__(self, repo: RepositoryInterface):
        self.__repo: RepositoryInterface = repo

    async def delete(self, id: str) -> None:
        await self.__repo.delete_item(id)
