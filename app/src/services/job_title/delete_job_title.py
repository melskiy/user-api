from src.base.job_title.store.interfaceses.repository_interface import RepositoryInterface


class DeleteJobTitleService:
    def __init__(self, repo: RepositoryInterface):
        self.__repo: RepositoryInterface = repo

    async def delete(self, id: str) -> None:
        await self.__repo.delete_item(id)
