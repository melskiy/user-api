from src.repository.Interfaceses.RepositoryInterface import RepositoryInterface
from src.factories.UserFactory import UserFactory

class UpdateUserService():
    async def update(self, repo:RepositoryInterface, name, surname, patronymic) -> None:
        user = UserFactory.create_user(id, name, surname, patronymic)
        await repo.update_item(user)