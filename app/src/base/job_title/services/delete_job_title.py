from src.base.job_title.store.interfaceses.repository_interface import JobTitleRepositoryInterface


class DeleteJobTitleService:
    def __init__(self, repo: JobTitleRepositoryInterface):
        self.__repo = repo

    async def delete(self, id: str) -> None:
        await self.__repo.delete_item(id)
