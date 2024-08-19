from fastapi.responses import JSONResponse

from src.base.job_title.exeptions.job_title_already_exists_error import JobTitleAlreadyExistsError


async def handle_job_title_exists(exc: JobTitleAlreadyExistsError):
    return JSONResponse(status_code=400, content={"detail": exc.message})
