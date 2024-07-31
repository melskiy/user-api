from src.repository.Interfaceses.RepositoryInterface import RepositoryInterface
from src.models.user import User

class GetUserService():
    async def get(self, repo:RepositoryInterface, id) -> User:
        return await repo.read_item(id)