from fastapi import APIRouter, Depends, status
from src.services.createUser import CreateUserService
from src.repository.Interfaceses.RepositoryInterface import RepositoryInterface
from src.repository.utils.getRepository import getRepository
from src.models.user import User

router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.post("/create", status_code=status.HTTP_200_OK, name="Создание пользователя по ФИО")
async def input_data(user: User, methods_service: CreateUserService = Depends(), repo: RepositoryInterface = Depends(getRepository)):
    return await methods_service.create(repo, user)
