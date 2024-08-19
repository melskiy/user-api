from fastapi import FastAPI

from src.base.job_title.exeptions.job_title_already_exists_error import JobTitleAlreadyExistsError
from src.base.job_title.exeptions.job_title_database_error import JobTitleDatabaseError
from src.base.job_title.exeptions.job_title_not_found_error import JobTitleNotFoundError
from src.base.job_title.web.exeptions.handlers import handle_job_title_not_found
from src.base.job_title.web.exeptions.handlers.handle_job_title_database_error import handle_job_title_database_error
from src.base.job_title.web.exeptions.handlers.handle_job_title_exists import handle_job_title_exists
from src.base.job_title.web.exeptions.handlers.job_title_error_handler import JobTitleErrorHandler
from src.core.Initializer.interfaces.Initialize import Initialize


class JobTitleExceptionHandlersInitializer(Initialize):

    def __init__(self, app: FastAPI):
        self.__app = app

    async def initialize(self):
        error_handler = JobTitleErrorHandler(self.__app)
        error_handler.register_handler(JobTitleDatabaseError, handle_job_title_database_error)
        error_handler.register_handler(JobTitleAlreadyExistsError, handle_job_title_exists)
        error_handler.register_handler(JobTitleNotFoundError, handle_job_title_not_found)
