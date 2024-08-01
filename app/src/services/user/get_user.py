from src.repository.Interfaceses.repository_interface import RepositoryInterface
from src.models.user import User


class GetUserService:
    async def get(self, repo: RepositoryInterface, id) -> User:
        return await repo.read_item(id)
