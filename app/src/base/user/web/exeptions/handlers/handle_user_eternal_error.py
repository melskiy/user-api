from urllib.request import Request

from starlette.responses import JSONResponse

from src.base.user.exeptions.user_eternal_error import UserEternalError


async def user_handle_eternal_error(request: Request, exc: UserEternalError):
    return JSONResponse(status_code=500, content={"detail": exc.message})
