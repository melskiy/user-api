from typing import Type

import redis
from rodi import Container

from src.core.Initializer.interfaces.Initialize import Initialize
from src.repository.utils.get_repository import get_repository
from src.services.user.create_user import CreateUserService
from src.services.user.delete_user import DeleteUserService
from src.services.user.get_user import GetUserService
from src.services.user.update_user import UpdateUserService


class ServiceInitializer(Initialize):

    def __init__(self, __container: Container):
        self.__container = __container

    def initialize(self):
        container = self.__container
        repo = container.resolve(get_repository)
        container.register(CreateUserService, instance=CreateUserService(repo))
        container.register(UpdateUserService, instance=UpdateUserService(repo))
        container.register(GetUserService, instance=GetUserService(repo))
        container.register(DeleteUserService, instance=DeleteUserService(repo))
