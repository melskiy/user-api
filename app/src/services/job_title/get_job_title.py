from src.base.job_title.store.interfaceses.repository_interface import RepositoryInterface
from src.base.job_title.models.job_title_base_model import JobTitleBaseModel

class GetJobTitleService:
    def __init__(self, repo: RepositoryInterface):
        self.__repo: RepositoryInterface = repo

    async def get(self, id) -> JobTitleBaseModel:
        return await self.__repo.read_item(id)
