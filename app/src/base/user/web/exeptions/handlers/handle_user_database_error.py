from urllib.request import Request

from starlette.responses import JSONResponse

from src.base.user.exeptions.user_database_error import UserDatabaseError


async def user_handle_database_error(request: Request, exc: UserDatabaseError):
    return JSONResponse(status_code=500, content={"detail": exc.message})
