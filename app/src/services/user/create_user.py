from src.repository.Interfaceses.repository_interface import RepositoryInterface
from src.models.user import User


class CreateUserService:
    async def create(self, repo: RepositoryInterface, user: User) -> User:
        await repo.create_item(user)
