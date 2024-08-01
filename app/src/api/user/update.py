from fastapi import APIRouter, Depends,status
from src.services.user.update_user import UpdateUserService
from src.repository.Interfaceses.repository_interface import RepositoryInterface
from src.repository.utils.get_repository import get_repository
from src.models.user import User

router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.put("/update", status_code=status.HTTP_200_OK, name="Изменение пользователя")
async def input_data(user:User, methods_service: UpdateUserService = Depends(), repo: RepositoryInterface = Depends(get_repository)):
    return await methods_service.update(repo,user)