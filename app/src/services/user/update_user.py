from src.repository.Interfaceses.repository_interface import RepositoryInterface
from src.models.user import User


class UpdateUserService:
    async def update(self, repo: RepositoryInterface, user: User) -> None:
        await repo.update_item(user)
