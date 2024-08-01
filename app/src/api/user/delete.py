from fastapi import APIRouter, Depends, status
from src.services.user.delete_user import DeleteUserService
from src.repository.Interfaceses.repository_interface import RepositoryInterface
from src.repository.utils.get_repository import get_repository

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.delete("/delete", status_code=status.HTTP_200_OK, name="Удаление пользователя")
async def input_data(
    methods_service: DeleteUserService = Depends(),
    repo: RepositoryInterface = Depends(get_repository),
    id: str = None,
):
    return await methods_service.delete(repo, id)
