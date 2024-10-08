from src.base.job_title.store.interfaceses.job_title_repository_interface import JobTitleRepositoryInterface
from src.base.job_title.models.job_title_base_model import JobTitleBaseModel


class GetJobTitleService:
    def __init__(self, repo: JobTitleRepositoryInterface):
        self.__repo = repo

    async def get(self, id) -> JobTitleBaseModel:
        return await self.__repo.read_item(id)
