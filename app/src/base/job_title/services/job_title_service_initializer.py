from src.base.job_title.store.interfaceses.job_title_repository_interface import JobTitleRepositoryInterface
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container
from src.base.job_title.services.create_job_title import CreateJobTitleService
from src.base.job_title.services.delete_job_title import DeleteJobTitleService
from src.base.job_title.services.get_job_title import GetJobTitleService
from src.base.job_title.services.update_job_title import UpdateJobTitleService


class JobTitleServiceInitializer(Initialize):

    async def initialize(self):
        repo = container.resolve(JobTitleRepositoryInterface)()
        container.register(CreateJobTitleService, instance=CreateJobTitleService(repo))
        container.register(UpdateJobTitleService, instance=UpdateJobTitleService(repo))
        container.register(GetJobTitleService, instance=GetJobTitleService(repo))
        container.register(DeleteJobTitleService, instance=DeleteJobTitleService(repo))
