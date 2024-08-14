from src.base.user.models.user_base_model import UserBaseModel


class RepositoryInterface:

    async def create_item(self, item) -> None:
        raise NotImplementedError

    async def read_item(self, item_id: str) -> UserBaseModel:
        raise NotImplementedError

    async def update_item(self, item: UserBaseModel) -> None:
        raise NotImplementedError

    async def delete_item(self, item_id: str) -> None:
        raise NotImplementedError
