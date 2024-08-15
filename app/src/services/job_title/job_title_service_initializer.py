from src.base.job_title.store.interfaceses.repository_interface import JobTitleRepositoryInterface
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container
from src.services.job_title.create_job_title import CreateJobTitleService
from src.services.job_title.delete_job_title import DeleteJobTitleService
from src.services.job_title.get_job_title import GetJobTitleService
from src.services.job_title.update_job_title import UpdateJobTitleService


class JobTitleServiceInitializer(Initialize):

    async def initialize(self):
        repo = container.resolve(JobTitleRepositoryInterface)
        container.register(CreateJobTitleService, instance=CreateJobTitleService(repo))
        container.register(UpdateJobTitleService, instance=UpdateJobTitleService(repo))
        container.register(GetJobTitleService, instance=UpdateJobTitleService(repo))
        container.register(DeleteJobTitleService, instance=UpdateJobTitleService(repo))
