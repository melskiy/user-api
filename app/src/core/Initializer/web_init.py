from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.base.job_title.web.job_title_web_initializer import JobTitleWebInitializer
from src.base.user.events.user_event_initilizer import UserEventInitializer
from src.base.user.web.user_web_initializer import UserWebInitializer
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container
from src.base.job_title.services.job_title_service_initializer import JobTitleServiceInitializer
from src.base.user.services.user_service_initializer import UserServiceInitializer


class WebInitializer(Initialize):

    async def initialize(self):
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

        origins = ["*"]

        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        container.register(FastAPI, instance=app)
        await UserEventInitializer().initialize()
        await UserServiceInitializer().initialize()
        await JobTitleServiceInitializer().initialize()
        await UserWebInitializer(app=container.resolve(FastAPI)).initialize()
        await JobTitleWebInitializer(app=container.resolve(FastAPI)).initialize()
