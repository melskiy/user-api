from fastapi import APIRouter, Depends, status
from src.services.user.get_user import GetUserService
from src.repository.Interfaceses.repository_interface import RepositoryInterface
from src.repository.utils.get_repository import get_repository
from src.models.user import User

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get(
    "/get",
    status_code=status.HTTP_200_OK,
    name="Получение пользователя",
    response_model=User,
)
async def input_data(
    methods_service: GetUserService = Depends(),
    repo: RepositoryInterface = Depends(get_repository),
    id: str = None,
):
    user = await methods_service.get(repo, id)
    return user
