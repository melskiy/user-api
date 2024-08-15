from src.base.job_title.store.interfaceses.repository_interface import RepositoryInterface
from src.base.job_title.models.job_title_base_model import JobTitleBaseModel


class UpdateJobTitleService:
    def __init__(self, repo: RepositoryInterface):
        self.__repo: RepositoryInterface = repo

    async def update(self, user: JobTitleBaseModel) -> None:
        await self.__repo.update_item(user)
