
from starlette import status
from rodi import Container
from src.base.user.models.user_base_model import UserBaseModel
from src.base.user.web.api.create import CreateDataView
from src.base.user.web.api.delete import DeleteDataView
from src.base.user.web.api.get import GetDataView
from src.base.user.web.api.update import UpdateDataView
from src.core.Initializer.interfaces.Initialize import Initialize
from src.services.user.create_user import CreateUserService
from src.services.user.delete_user import DeleteUserService
from src.services.user.get_user import GetUserService
from src.services.user.update_user import UpdateUserService


class WebInitializer(Initialize):

    def __init__(self, __container: Container, router):
        self.__container = __container
        self.router = router
    def initialize(self):
        container = self.__container
        router = self.router

        router.add_api_route("/create", CreateDataView(container.resolve(CreateUserService)).__call__,
                             status_code=status.HTTP_200_OK, name="Создание пользователя",
                             response_model=UserBaseModel, methods=["POST"])

        router.add_api_route("/update", UpdateDataView(container.resolve(UpdateUserService)).__call__,
                             status_code=status.HTTP_200_OK, name="Обновление пользователя", methods=["PUT"])

        router.add_api_route("/delete", DeleteDataView(container.resolve(DeleteUserService)).__call__,
                             status_code=status.HTTP_200_OK, name="Удаление пользователя", methods=["Delete"])

        router.add_api_route("/get", GetDataView(container.resolve(GetUserService)).__call__,
                             status_code=status.HTTP_200_OK, name="Получение пользователя",
                             methods=["GET"])

        return router

