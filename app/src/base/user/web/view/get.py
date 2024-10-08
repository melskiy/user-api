from src.base.user.models.user_base_model import UserBaseModel
from src.base.user.services.get_user import GetUserService


class GetDataView:
    def __init__(self, service: GetUserService):
        self.service: GetUserService = service

    async def __call__(self, id: str) -> UserBaseModel:
        return await self.service.get(id)
