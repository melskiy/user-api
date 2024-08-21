from src.base.job_title.models.job_title_base_model import JobTitleBaseModel
from src.base.job_title.store.interfaceses.job_title_repository_interface import JobTitleRepositoryInterface


class CreateJobTitleService:
    def __init__(self, repo: JobTitleRepositoryInterface):
        self.__repo = repo

    async def create(self, user: JobTitleBaseModel) -> None:
        await self.__repo.create_item(user)


