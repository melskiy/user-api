from src.repository.Interfaceses.RepositoryInterface import RepositoryInterface

class GetUserService():
    async def get(self, repo:RepositoryInterface, id) -> None:
        await repo.read_item(id)