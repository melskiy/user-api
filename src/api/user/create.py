from fastapi import APIRouter, Depends,status
from src.services.createUser import CreateUserService

router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.post("/create", status_code=status.HTTP_200_OK, name="Создание пользователя по ФИО")
async def input_data(methods_service: CreateUserService = Depends()):
    return await methods_service.create()
