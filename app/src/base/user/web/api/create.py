from fastapi import APIRouter, Depends, status
from src.services.user.create_user import CreateUserService
from src.repository.interfaceses.repository_interface import RepositoryInterface
from src.repository.utils.get_repository import get_repository
from src.base.user.models.user_base_model import UserBaseModel

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/create", status_code=status.HTTP_200_OK, name="Создание пользователя", response_model = UserBaseModel)
async def input_data(
    user: UserBaseModel,
    methods_service: CreateUserService = Depends(),
    repo: RepositoryInterface = Depends(get_repository),
):
    return await methods_service.create(repo, user)
