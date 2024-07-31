from fastapi import FastAPI

from src.api.base_router import router

from fastapi.middleware.cors import CORSMiddleware

origins = [
   '*'
]
tags_dict = [
    {
        'name': 'create',
        'description': 'Создать пользователя',
    },
    {
        'name': 'get',
        'description': 'Получить пользователя'
    },
    {
        'name': 'update',
        'description': 'Редактировать пользователя'
    },
    {
        'name': 'delete',
        'description': 'Удалить пользователя'
    }
]

app = FastAPI(
    title="User API",
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

app.include_router(router)