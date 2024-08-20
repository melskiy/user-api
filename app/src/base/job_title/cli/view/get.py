import asyncclick as click
from src.base.job_title.services.get_job_title import GetJobTitleService
from src.base.job_title.models.job_title_base_model import JobTitleBaseModel


class GetJobTitleConsoleView(click.Command):
    def __init__(self, service: GetJobTitleService):
        self.service: GetJobTitleService = service
        super().__init__(name='get', params=[click.Argument(['id'])])

    async def invoke(self, ctx) -> JobTitleBaseModel:
        id = ctx.params['id']
        return await self.service.get(id)
