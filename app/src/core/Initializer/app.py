import uvicorn
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from src.core.Initializer.interfaces.Initialize import Initialize

from rodi import Container

from src.core.settings import settings


class FastApiInitializer(Initialize):

    def __init__(self, __container: Container):
        self.__container = __container

    def initialize(self):
        container = self.__container

        origins = ["*"]
        tags_dict = [
            {"name": "create", "description": "Создать пользователя"},
            {"name": "get", "description": "Получить пользователя"},
            {"name": "update", "description": "Редактировать пользователя"},
            {"name": "delete", "description": "Удалить пользователя"},
        ]

        app = FastAPI(
            title="UserBaseModel API",
            description="Работа с сущностью User",
            version="0.1.0",
            openapi_tags=tags_dict,
        )

        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        app.include_router(container.resolve(APIRouter))

        uvicorn.run(
            app,
            host=settings.host,
            port=settings.port,
        )
