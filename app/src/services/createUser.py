from src.factories.UserFactory import UserFactory
from src.repository.InMemoryDatabase import InMemoryDatabase

# Service for creating a new user in the database.
class CreateUserService():
    async def create(self, repo, id, name, surname, patronymic) -> None:
        user = UserFactory.create_user(id, name, surname, patronymic)
        await repo.create_item(user)
        
        
        