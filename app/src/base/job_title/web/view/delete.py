from src.base.job_title.services.delete_job_title import DeleteJobTitleService


class DeleteJobTitleView:
    def __init__(self, __service: DeleteJobTitleService):
        self.__service: DeleteJobTitleService = __service

    async def __call__(self, id: str) -> None:
        return await self.__service.delete(id)
