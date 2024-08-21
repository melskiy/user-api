from fastapi import FastAPI
from starlette import status

from src.base.job_title.models.job_title_base_model import JobTitleBaseModel
from src.base.user.web.exeptions.user_exception_handlers_initializer import UserExceptionHandlersInitializer
from src.base.user.web.view.create import CreateDataView
from src.base.user.web.view.delete import DeleteDataView
from src.base.user.web.view.get import GetDataView
from src.base.user.web.view.update import UpdateDataView
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container
from src.base.user.services.create_user import CreateUserService
from src.base.user.services.delete_user import DeleteUserService
from src.base.user.services.get_user import GetUserService
from src.base.user.services.update_user import UpdateUserService


class UserWebInitializer(Initialize):

    def __init__(self, app: FastAPI):
        self.app = app

    async def initialize(self):
        app = self.app
        app.add_api_route("/create",
                          endpoint=CreateDataView(container.resolve(CreateUserService)).__call__,
                          status_code=status.HTTP_200_OK, name="Создание пользователя", methods=["POST"])

        app.add_api_route("/update",
                          endpoint=UpdateDataView(container.resolve(UpdateUserService)).__call__,
                          status_code=status.HTTP_200_OK, name="Обновление пользователя", methods=["PUT"])

        app.add_api_route("/delete",
                          endpoint=DeleteDataView(container.resolve(DeleteUserService)).__call__,
                          status_code=status.HTTP_200_OK, name="Удаление пользователя", methods=["Delete"])

        app.add_api_route("/get",
                          endpoint=GetDataView(container.resolve(GetUserService)).__call__,
                          status_code=status.HTTP_200_OK, name="Получение пользователя",
                          methods=["GET"])

        await UserExceptionHandlersInitializer(app).initialize()
