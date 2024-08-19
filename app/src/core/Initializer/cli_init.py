from src.base.user.events.user_event_initilizer import UserEventInitializer
from src.core.Initializer.interfaces.Initialize import Initialize
from src.base.job_title.services.job_title_service_initializer import JobTitleServiceInitializer
from src.base.user.services.user_service_initializer import UserServiceInitializer


class CliInitializer(Initialize):

    async def initialize(self):
        await UserEventInitializer().initialize()
        await UserServiceInitializer().initialize()
        await JobTitleServiceInitializer().initialize()
