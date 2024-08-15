from fastapi import HTTPException
from typing import Optional

from redis import Redis

from src.base.user.models.user_base_model import UserBaseModel

from src.base.job_title.store.interfaceses.repository_interface import RepositoryInterface
from redis.exceptions import RedisError


class UserRedisDatabase(RepositoryInterface):
    def __init__(self, session: Redis):
        self.__session = session

    async def create_item(self, item: UserBaseModel) -> UserBaseModel:
        async with self.__session as session:
            try:
                existing_user = await session.get(f"user:email:{item.email}")
                if existing_user:
                    raise HTTPException(status_code=400, detail="Email already exists")
                await session.set(f"user:email:{item.email}", item.user_id)
                await session.set(f"user:{item.user_id}", item.model_dump_json())
                return item
            except RedisError as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def read_item(self, item_id: str) -> Optional[UserBaseModel]:
        async with self.__session as session:
            try:
                item_data = await session.get(f"user:{item_id}")
                if item_data:
                    return UserBaseModel.model_validate_json(item_data)
                raise HTTPException(status_code=404, detail="Item not found")
            except RedisError as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def update_item(self, item: UserBaseModel) -> None:
        async with self.__session as session:
            try:
                item_data = await session.get(f"user:{item.user_id}")
                if item_data:
                    await session.set(f"user:{item.user_id}", item.model_dump_json())
                else:
                    raise HTTPException(status_code=404, detail="Item not found")
            except RedisError as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def delete_item(self, item_id: str) -> None:
        async with self.__session as session:
            try:
                await session.delete(f"user:{item_id}")
            except RedisError as e:
                raise HTTPException(status_code=500, detail=str(e))
