from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from src.core.Initializer.web_init import WebInitializer

from rodi import Container

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
container =
app.include_router(WebInitializer(container).initialize())

