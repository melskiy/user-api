import asyncclick as click
from src.base.user.services.update_user import UpdateUserService


class UpdateJobTitleConsoleView(click.Command):
    def __init__(self, service: UpdateUserService):
        self.service: UpdateUserService = service
        super().__init__(name='update', params=[click.Argument(['user'])])

    async def invoke(self, ctx) -> None:
        user = ctx.params['user']
        return await self.service.update(user)
