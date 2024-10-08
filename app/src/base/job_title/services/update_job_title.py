from src.base.job_title.store.interfaceses.job_title_repository_interface import JobTitleRepositoryInterface

from src.base.job_title.models.job_title_base_model import JobTitleBaseModel


class UpdateJobTitleService:
    def __init__(self, repo: JobTitleRepositoryInterface):
        self.__repo = repo

    async def update(self, user: JobTitleBaseModel) -> None:
        await self.__repo.update_item(user)
