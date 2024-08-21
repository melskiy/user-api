from src.base.user.store.interfaceses.user_repository_interface import UserRepositoryInterface
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container
from src.events.event_manger import EventManager
from src.base.user.services.create_user import CreateUserService
from src.base.user.services.delete_user import DeleteUserService
from src.base.user.services.get_user import GetUserService
from src.base.user.services.update_user import UpdateUserService


class UserServiceInitializer(Initialize):

    async def initialize(self):
        repo = container.resolve(UserRepositoryInterface)()
        container.register(CreateUserService, instance=CreateUserService(repo, container.resolve(EventManager)))
        container.register(UpdateUserService, instance=UpdateUserService(repo))
        container.register(GetUserService, instance=GetUserService(repo))
        container.register(DeleteUserService, instance=DeleteUserService(repo))

