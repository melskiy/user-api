from fastapi import APIRouter, Depends,status
from src.services.deleteUser import DeleteUserService
router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.post("/delete", status_code=status.HTTP_200_OK, name="Удаление пользователя по ФИО")
async def input_data(methods_service: DeleteUserService = Depends()):
    return await methods_service.delete()