from fastapi import APIRouter, status

from src.services.user.create_user import CreateUserService
from src.base.user.models.user_base_model import UserBaseModel

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/create", status_code=status.HTTP_200_OK, name="Создание пользователя", response_model = UserBaseModel)
async def input_data(
    user: UserBaseModel,
):
    method = CreateUserService()
    return await method.create(user)
