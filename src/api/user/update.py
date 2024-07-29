from fastapi import APIRouter, Depends,status
from src.services.updateUser import UpdateUserService
router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.post("/update", status_code=status.HTTP_200_OK, name="Изменение пользователя по ФИО")
async def input_data(methods_service: UpdateUserService = Depends()):
    return await methods_service.update()