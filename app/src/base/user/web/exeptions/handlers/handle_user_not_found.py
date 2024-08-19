from starlette.responses import JSONResponse

from src.base.user.exeptions.user_not_found_error import UserNotFoundError


async def handle_user_not_found(exc: UserNotFoundError):
    return JSONResponse(status_code=404, content={"detail": exc.message})
