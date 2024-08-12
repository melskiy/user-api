from src.services.user.update_user import UpdateUserService
from src.base.user.models.user_base_model import UserBaseModel


class UpdateDataView:
    def __init__(self, service: UpdateUserService):
        self.service: UpdateUserService = service

    async def __call__(self, user: UserBaseModel) -> None:
        return await self.service.update(user)
