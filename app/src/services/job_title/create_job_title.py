from src.base.job_title.models.job_title_base_model import JobTitleBaseModel
from src.base.job_title.store.interfaceses.repository_interface import RepositoryInterface


class CreateJobTitleService:
    def __init__(self, repo: RepositoryInterface):
        self.__repo: RepositoryInterface = repo

    async def create(self, user: JobTitleBaseModel) -> None:
        success = await self.__repo.create_item(user)
