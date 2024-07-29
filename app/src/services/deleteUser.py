from src.repository.Interfaceses.RepositoryInterface import RepositoryInterface

class DeleteUserService():
    async def delete(self, repo:RepositoryInterface, id) -> None:
        return repo.delete_item(id)