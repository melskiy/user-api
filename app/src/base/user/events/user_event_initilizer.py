from src.base.user.events.user_created_event_handler import UserCreateEventHandler
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container
from src.events.event_manager_factory import EventManagerFactory
from src.events.event_manger import EventManager


class UserEventInitializer(Initialize):

    async def initialize(self):

        event_manager = EventManagerFactory()()

        event_manager.subscribe(UserCreateEventHandler())
        container.register(EventManager, instance=event_manager)
