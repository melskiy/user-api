from rodi import Container
from src.core.Initializer.interfaces.Initialize import Initialize
from src.repository.utils.get_repository import get_repository


class RepositoryInitializer(Initialize):

    def __init__(self, __container: Container):
        self.__container = __container

    def initialize(self):
        container = self.__container
        container.register(get_repository, instance=get_repository())
