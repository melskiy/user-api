from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container
from src.core.settings.settings import Settings
from src.services.job_title.create_job_title import CreateJobTitleService
from src.services.job_title.delete_job_title import DeleteJobTitleService
from src.services.job_title.get_job_title import GetJobTitleService
from src.services.job_title.update_job_title import UpdateJobTitleService


class JobTitleInitializer(Initialize):

    async def initialize(self):
        settings = container.resolve(Settings)
        repo = container.resolve(settings.repository_type)
        container.register(CreateJobTitleService, instance=CreateJobTitleService(repo))
        container.register(UpdateJobTitleService, instance=UpdateJobTitleService(repo))
        container.register(GetJobTitleService, instance=UpdateJobTitleService(repo))
        container.register(DeleteJobTitleService, instance=UpdateJobTitleService(repo))
