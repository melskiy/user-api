from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.base.user.web.api.base_router import router
from src.repository.postgres_database import PostgresDatabase
from src.repository.redis_database import RedisDatabase
from src.factories.repository_factory import RepositoryFactory

RepositoryFactory.register("postgresql", PostgresDatabase)
RepositoryFactory.register("redis", RedisDatabase)


origins = ["*"]
tags_dict = [
    {"name": "create", "description": "Создать пользователя"},
    {"name": "get", "description": "Получить пользователя"},
    {"name": "update", "description": "Редактировать пользователя"},
    {"name": "delete", "description": "Удалить пользователя"},
]

app = FastAPI(
    title="UserBaseModel API",
    description="Работа с сущностью UserBaseModel",
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

app.include_router(router)
