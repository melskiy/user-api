from src.base.job_title.web.job_title_web_initializer import JobTitleWebInitializer
from src.base.user.events.user_event_initilizer import UserEventInitializer
from src.base.user.web.user_web_initializer import UserWebInitializer
from src.core.Initializer.interfaces.Initialize import Initialize
from src.services.job_title.job_title_service_initializer import JobTitleServiceInitializer
from src.services.user.user_service_initializer import UserServiceInitializer


class CliInitializer(Initialize):

    async def initialize(self):
        await UserServiceInitializer().initialize()
        await JobTitleServiceInitializer().initialize()
        await UserEventInitializer().initialize()
        await UserWebInitializer().initialize()
        await JobTitleWebInitializer().initialize()

