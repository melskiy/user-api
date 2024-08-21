import asyncclick as click

from src.base.job_title.services.delete_job_title import DeleteJobTitleService


class DeleteJobTitleConsoleView(click.Command):
    def __init__(self, service: DeleteJobTitleService):
        self.__service: DeleteJobTitleService = service
        super().__init__(name='delete', params=[click.Argument(['id'])])

    async def invoke(self, ctx) -> None:
        id:str = ctx.params['id']
        return await self.__service.delete(id)
