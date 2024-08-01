from src.repository.interfaceses.repository_interface import RepositoryInterface


class DeleteUserService:
    async def delete(self, repo: RepositoryInterface, id) -> None:
        await repo.delete_item(id)
