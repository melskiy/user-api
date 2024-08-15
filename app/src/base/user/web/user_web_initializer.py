from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container
from src.core.settings.settings import Settings
from src.events.event_manger import EventManager
from src.services.user.create_user import CreateUserService
from src.services.user.delete_user import DeleteUserService
from src.services.user.get_user import GetUserService
from src.services.user.update_user import UpdateUserService


class UserWebInitializer(Initialize):

    async def initialize(self):
        settings = container.resolve(Settings)
        repo = container.resolve(settings.repository_type)

        container.register(CreateUserService, instance=CreateUserService(repo, container.resolve(EventManager)))
        container.register(UpdateUserService, instance=UpdateUserService(repo))
        container.register(GetUserService, instance=GetUserService(repo))
        container.register(DeleteUserService, instance=DeleteUserService(repo))

