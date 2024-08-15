from starlette import status

from src.base.job_title.models.job_title_base_model import JobTitleBaseModel
from src.base.job_title.web.view.create import CreateJobTitleView
from src.base.user.web.view.create import CreateDataView
from src.base.user.web.view.delete import DeleteDataView
from src.base.user.web.view.get import GetDataView
from src.base.user.web.view.update import UpdateDataView
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container
from src.services.job_title.create_job_title import CreateJobTitleService
from src.services.user.create_user import CreateUserService
from src.services.user.delete_user import DeleteUserService
from src.services.user.get_user import GetUserService
from src.services.user.update_user import UpdateUserService


class UserWebInitializer(Initialize):

    def __init__(self, app):
        self.app = app

    async def initialize(self):
        app = self.app
        app.add_api_route("/create", endpoint=CreateDataView(container.resolve(CreateUserService)).__call__,
                          status_code=status.HTTP_200_OK, name="Создание пользователя", methods=["POST"])

        app.add_api_route("/update", endpoint=UpdateDataView(container.resolve(UpdateUserService)).__call__,
                          status_code=status.HTTP_200_OK, name="Обновление пользователя", methods=["PUT"])

        app.add_api_route("/delete", endpoint=DeleteDataView(container.resolve(DeleteUserService)).__call__,
                          status_code=status.HTTP_200_OK, name="Удаление пользователя", methods=["Delete"])

        app.add_api_route("/get", endpoint=GetDataView(container.resolve(GetUserService)).__call__,
                          status_code=status.HTTP_200_OK, name="Получение пользователя",
                          methods=["GET"], response_model=JobTitleBaseModel)
