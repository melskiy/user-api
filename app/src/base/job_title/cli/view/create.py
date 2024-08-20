import asyncclick as click

from src.base.job_title.services.create_job_title import CreateJobTitleService
from src.base.job_title.models.job_title_base_model import JobTitleBaseModel


class CreateJobTitleConsoleView(click.Command):
    def __init__(self, service: CreateJobTitleService):
        super().__init__(name='create', params=[click.Argument(['user'])])
        self.__service: CreateJobTitleService = service

    async def invoke(self, ctx) -> None:
        user: JobTitleBaseModel = ctx.params['user']
        await self.__service.create(user)
