from src.services.job_title.create_job_title import CreateJobTitleService
from src.base.job_title.models.job_title_base_model import JobTitleBaseModel


class CreateJobTitleView:
    def __init__(self, service: CreateJobTitleService):
        self.__service: CreateJobTitleService = service

    async def __call__(self, user: JobTitleBaseModel) -> None:
        await self.__service.create(user)
