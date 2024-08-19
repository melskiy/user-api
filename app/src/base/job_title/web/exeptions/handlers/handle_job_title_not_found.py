from starlette.responses import JSONResponse

from src.base.job_title.exeptions.job_title_not_found_error import JobTitleNotFoundError


async def handle_job_title_not_found(exc: JobTitleNotFoundError):
    return JSONResponse(status_code=404, content={"detail": exc.message})
