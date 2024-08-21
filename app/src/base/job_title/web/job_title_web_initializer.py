from fastapi import FastAPI
from starlette import status

from src.base.job_title.services.get_job_title import GetJobTitleService
from src.base.job_title.web.exeptions.job_title_exception_handlers_initializer import \
    JobTitleExceptionHandlersInitializer
from src.base.job_title.web.view.create import CreateJobTitleView
from src.base.job_title.web.view.get import GetJobTitleView
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container
from src.base.job_title.services.create_job_title import CreateJobTitleService


class JobTitleWebInitializer(Initialize):

    def __init__(self, app: FastAPI):
        self.app = app

    async def initialize(self):
        app = self.app
        app.add_api_route("/create_title_job",
                          endpoint=CreateJobTitleView(container.resolve(CreateJobTitleService)).__call__,
                          status_code=status.HTTP_200_OK, name="Создание должности", methods=["POST"])
        app.add_api_route("/get_title_job",
                          endpoint=GetJobTitleView(container.resolve(GetJobTitleService)).__call__,
                          status_code=status.HTTP_200_OK, name="Создание должности", methods=["GET"])
        await JobTitleExceptionHandlersInitializer(app).initialize()
