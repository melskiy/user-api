from urllib.request import Request

from starlette.responses import JSONResponse

from src.base.job_title.exeptions.job_title_eternal_error import JobTitleEternalError


async def handle_job_title_eternal_error(request: Request, exc: JobTitleEternalError):
    return JSONResponse(status_code=500, content={"detail": exc.message})
