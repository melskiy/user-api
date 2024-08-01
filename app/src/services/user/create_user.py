from src.repository.interfaceses.repository_interface import RepositoryInterface
from src.models.user import User


class CreateUserService:
    async def create(self, repo: RepositoryInterface, user: User) -> User:
        return await repo.create_item(user)
