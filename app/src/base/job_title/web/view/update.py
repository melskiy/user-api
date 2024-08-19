from src.base.user.services.update_user import UpdateUserService
from src.base.job_title.models.job_title_base_model import JobTitleBaseModel


class UpdateJobTitleView:
    def __init__(self, service: UpdateUserService):
        self.service: UpdateUserService = service

    async def __call__(self, user: JobTitleBaseModel) -> None:
        return await self.service.update(user)
