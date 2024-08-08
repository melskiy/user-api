from fastapi import APIRouter, Depends, status
from src.services.user.delete_user import DeleteUserService

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.delete("/delete", status_code=status.HTTP_200_OK, name="Удаление пользователя")
async def input_data(
    id: str = None,
):
    method = DeleteUserService()
    return await method.delete(id)
