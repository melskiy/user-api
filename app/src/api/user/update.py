from fastapi import APIRouter, Depends,status
from src.services.updateUser import UpdateUserService
from src.repository.Interfaceses.RepositoryInterface import RepositoryInterface
from src.repository.utils.getRepository import getRepository
from src.models.user import User

router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.put("/update", status_code=status.HTTP_200_OK, name="Изменение пользователя по ФИО")
async def input_data(user:User, methods_service: UpdateUserService = Depends(), repo: RepositoryInterface = Depends(getRepository)):
    return await methods_service.update(repo,user)