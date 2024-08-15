from src.services.job_title.get_job_title import GetJobTitleService
from src.base.job_title.models.job_title_base_model import JobTitleBaseModel


class GetJobTitleView:
    def __init__(self, service: GetJobTitleService):
        self.service: GetJobTitleService = service

    async def __call__(self, id: str) -> JobTitleBaseModel:
        return await self.service.get(id)
