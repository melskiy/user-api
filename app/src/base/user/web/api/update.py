from fastapi import APIRouter, Depends, status

from src.services.user.update_user import UpdateUserService
from src.base.user.models.user_base_model import UserBaseModel

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.put("/update", status_code=status.HTTP_200_OK, name="Изменение пользователя")
async def input_data(
    user: UserBaseModel,
):
    method = UpdateUserService()
    return await method.update(user)
