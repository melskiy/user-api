from fastapi.responses import JSONResponse
from src.base.user.exeptions.user_already_exists_error import UserAlreadyExistsError


async def user_handle_user_exists(exc: UserAlreadyExistsError):
    return JSONResponse(status_code=400, content={"detail": exc.message})
