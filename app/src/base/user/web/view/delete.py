from src.base.user.services.delete_user import DeleteUserService


class DeleteDataView:
    def __init__(self, __service: DeleteUserService):
        self.__service: DeleteUserService = __service

    async def __call__(self, id: str) -> None:
        return await self.__service.delete(id)
