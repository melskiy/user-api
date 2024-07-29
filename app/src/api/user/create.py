from fastapi import APIRouter, Depends, status
from src.services.createUser import CreateUserService
from src.repository.Interfaceses.RepositoryInterface import RepositoryInterface
from src.repository.utils.getRepository import getRepository

router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.post("/create", status_code=status.HTTP_200_OK, name="Создание пользователя по ФИО")
async def input_data(methods_service: CreateUserService = Depends(), repo: RepositoryInterface = Depends(getRepository), id: str = None, name: str = None, surname: str = None, patronymic: str = None):
    return await methods_service.create(repo, id, name, surname, patronymic)
