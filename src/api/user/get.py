from fastapi import APIRouter, Depends,status
from src.services.getUser import GetUserService

router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.post("/get", status_code=status.HTTP_200_OK, name="Получение пользователя по ФИО")
async def input_data(methods_service: GetUserService = Depends()):
    return await methods_service.get()