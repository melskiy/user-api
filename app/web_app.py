import asyncio

import uvicorn
from fastapi import FastAPI
from starlette import status
from starlette.middleware.cors import CORSMiddleware

from src.base.user.models.user_base_model import UserBaseModel
from src.base.user.web.view.create import CreateDataView
from src.base.user.web.view.delete import DeleteDataView
from src.base.user.web.view.get import GetDataView
from src.base.user.web.view.update import UpdateDataView
from src.core.Initializer.app_init import AppInitializer
from src.core.ioc.ioc import container
from src.core.settings.settings import Settings
from src.services.user.create_user import CreateUserService
from src.services.user.delete_user import DeleteUserService
from src.services.user.get_user import GetUserService
from src.services.user.update_user import UpdateUserService

settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8",
)

tags_dict = [
    {"name": "create", "description": "Создать пользователя"},
    {"name": "get", "description": "Получить пользователя"},
    {"name": "update", "description": "Редактировать пользователя"},
    {"name": "delete", "description": "Удалить пользователя"},
]

app = FastAPI(title="UserBaseModel API",
              description="Работа с сущностью User",
              version="0.1.0",
              openapi_tags=tags_dict, )


async def run() -> None:
    await AppInitializer().initialize()
    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_api_route("/create", endpoint=CreateDataView(container.resolve(CreateUserService)).__call__,
                      status_code=status.HTTP_200_OK, name="Создание пользователя", methods=["POST"])

    app.add_api_route("/update", UpdateDataView(container.resolve(UpdateUserService)).__call__,
                      status_code=status.HTTP_200_OK, name="Обновление пользователя", methods=["PUT"])

    app.add_api_route("/delete", DeleteDataView(container.resolve(DeleteUserService)).__call__,
                      status_code=status.HTTP_200_OK, name="Удаление пользователя", methods=["Delete"])

    app.add_api_route("/get", GetDataView(container.resolve(GetUserService)).__call__,
                      status_code=status.HTTP_200_OK, name="Получение пользователя",
                      methods=["GET"], response_model=UserBaseModel)


if __name__ == '__main__':
    asyncio.run(run())
    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port,
    )
