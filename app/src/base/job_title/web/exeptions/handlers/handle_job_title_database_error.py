from starlette.responses import JSONResponse

from src.base.job_title.exeptions.job_title_database_error import JobTitleDatabaseError


async def handle_job_title_database_error(exc: JobTitleDatabaseError):
    return JSONResponse(status_code=500, content={"detail": exc.message})
