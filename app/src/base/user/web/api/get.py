from fastapi import APIRouter, status

from src.services.user.get_user import GetUserService
from src.base.user.models.user_base_model import UserBaseModel

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get(
    "/get",
    status_code=status.HTTP_200_OK,
    name="Получение пользователя",
    response_model=UserBaseModel,
)
async def input_data(
    id: str = None,
):
    method = GetUserService()
    user = await method.get(id)
    return user
