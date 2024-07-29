from fastapi import APIRouter, Depends,status
from src.services.deleteUser import DeleteUserService
from src.repository.Interfaceses.RepositoryInterface import RepositoryInterface
from src.repository.utils.getRepository import getRepository

router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.delete("/delete", status_code=status.HTTP_200_OK, name="Удаление пользователя по ФИО")
async def input_data(methods_service: DeleteUserService = Depends(), repo: RepositoryInterface = Depends(getRepository), id: str = None):
    return await methods_service.delete(repo, id)