from starlette import status

from src.base.job_title.web.view.create import CreateJobTitleView
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container
from src.services.job_title.create_job_title import CreateJobTitleService


class JobTitleWebInitializer(Initialize):

    def __init__(self, app):
        self.app = app

    async def initialize(self):
        app = self.app
        app.add_api_route("/create_title_job",
                          endpoint=CreateJobTitleView(container.resolve(CreateJobTitleService)).__call__,
                          status_code=status.HTTP_200_OK, name="Создание должности", methods=["POST"])