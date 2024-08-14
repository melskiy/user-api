from rodi import Container

from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.settings.settings import Settings
from src.factories.factory import Factory
from src.repository.utils.get_repository import get_repository


class RepositoryInitializer(Initialize):

    def __init__(self, __container: Container, settings: Settings):
        self.__container = __container
        self.__settings = settings

    def initialize(self):
        container = self.__container
        settings = self.__settings
        container.register(get_repository, instance=get_repository(Factory.create(settings.repository_type + "session"),
                                                                   settings.repository_type))
