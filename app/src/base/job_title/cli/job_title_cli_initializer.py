from src.base.job_title.cli.view.create import CreateJobTitleConsoleView
from src.base.job_title.cli.view.delete import DeleteJobTitleConsoleView
from src.base.job_title.cli.view.get import GetJobTitleConsoleView
from src.base.job_title.cli.view.update import UpdateJobTitleConsoleView
from src.base.job_title.services.create_job_title import CreateJobTitleService
from src.base.job_title.services.delete_job_title import DeleteJobTitleService
from src.base.job_title.services.get_job_title import GetJobTitleService
from src.base.job_title.services.update_job_title import UpdateJobTitleService
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container
import asyncclick as click


class JobTitleCliInitializer(Initialize):

    async def initialize(self):
        cli = container.resolve(click)
        cli.add_command(CreateJobTitleConsoleView(service=container.resolve(CreateJobTitleService)))
        cli.add_command(DeleteJobTitleConsoleView(service=container.resolve(DeleteJobTitleService)))
        cli.add_command(GetJobTitleConsoleView(service=container.resolve(GetJobTitleService)))
        cli.add_command(UpdateJobTitleConsoleView(service=container.resolve(UpdateJobTitleService)))
