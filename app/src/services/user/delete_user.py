from src.repository.interfaceses.repository_interface import RepositoryInterface
from src.repository.utils.get_repository import get_repository


class DeleteUserService:
    def __init__(self):
        self.repo: RepositoryInterface = get_repository()

    async def delete(self, id: str) -> None:
        await self.repo.delete_item(id)
