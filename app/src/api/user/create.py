from fastapi import APIRouter, Depends, status
from src.services.user.create_user import CreateUserService
from src.repository.Interfaceses.repository_interface import RepositoryInterface
from src.repository.utils.get_repository import get_repository
from src.models.user import User

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/create", status_code=status.HTTP_200_OK, name="Создание пользователя")
async def input_data(
    user: User,
    methods_service: CreateUserService = Depends(),
    repo: RepositoryInterface = Depends(get_repository),
):
    return await methods_service.create(repo, user)
