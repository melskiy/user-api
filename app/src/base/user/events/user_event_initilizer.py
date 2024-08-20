from src.base.user.events.user_create_event import UserCreateSubscriber
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container
from src.events.event_manager_factory import EventManagerFactory
from src.events.event_manger import EventManager


class UserEventInitializer(Initialize):

    async def initialize(self):

        manager = EventManagerFactory()()

        manager.subscribe(UserCreateSubscriber())
        container.register(EventManager, instance=manager)
