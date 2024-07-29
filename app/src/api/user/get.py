from fastapi import APIRouter, Depends,status
from src.services.getUser import GetUserService
from src.repository.Interfaceses.RepositoryInterface import RepositoryInterface
from src.repository.utils.getRepository import getRepository

router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.get("/get", status_code=status.HTTP_200_OK, name="Получение пользователя по ФИО")
async def input_data(methods_service: GetUserService = Depends(), repo: RepositoryInterface = Depends(getRepository), id: str = None):
    return await methods_service.get(repo, id)