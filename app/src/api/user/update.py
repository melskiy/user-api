from fastapi import APIRouter, Depends,status
from src.services.updateUser import UpdateUserService
from src.repository.Interfaceses.RepositoryInterface import RepositoryInterface
from src.repository.utils.getRepository import getRepository
router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.put("/update", status_code=status.HTTP_200_OK, name="Изменение пользователя по ФИО")
async def input_data(methods_service: UpdateUserService = Depends(), repo: RepositoryInterface = Depends(getRepository), id: str = None, name: str = None, surname: str = None, patronymic: str = None):
    return await methods_service.update(repo, id, name, surname, patronymic)