from src.models.user import User


class CreateUserService:
    async def create(self, repo, user: User) -> None:
        await repo.create_item(user)
