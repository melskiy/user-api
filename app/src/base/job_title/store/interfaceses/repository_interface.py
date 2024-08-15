from src.base.job_title.models.job_title_base_model import JobTitleBaseModel


class RepositoryInterface:

    async def create_item(self, item) -> None:
        raise NotImplementedError

    async def read_item(self, item_id: str) -> JobTitleBaseModel:
        raise NotImplementedError

    async def update_item(self, item: JobTitleBaseModel) -> None:
        raise NotImplementedError

    async def delete_item(self, item_id: str) -> None:
        raise NotImplementedError
