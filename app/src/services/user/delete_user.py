from src.repository.interfaceses.repository_interface import RepositoryInterface


class DeleteUserService:
    def __init__(self, repo: RepositoryInterface):
        self.repo: RepositoryInterface = repo

    async def delete(self, id: str) -> None:
        await self.repo.delete_item(id)
