from fastapi import HTTPException
from typing import Optional

from redis import Redis

from src.base.job_title.models.job_title_base_model import JobTitleBaseModel
from src.base.job_title.store.interfaceses.repository_interface import RepositoryInterface
from redis.exceptions import RedisError


class JobTitleRedisDatabase(RepositoryInterface):
    def __init__(self, session: Redis):
        self.__session = session

    async def create_item(self, item: JobTitleBaseModel) -> JobTitleBaseModel:
        async with self.__session as session:
            try:
                await session.set(f"job_title:{item.job_title_id}", item.model_dump_json())
                return item
            except RedisError as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def read_item(self, item_id: str) -> Optional[JobTitleBaseModel]:
        async with self.__session as session:
            try:
                item_data = await session.get(f"job_title:{item_id}")
                if item_data:
                    return JobTitleBaseModel.model_validate_json(item_data)
                raise HTTPException(status_code=404, detail="Item not found")
            except RedisError as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def update_item(self, item: JobTitleBaseModel) -> None:
        async with self.__session as session:
            try:
                item_data = await session.get(f"job_title:{item.job_title_id}")
                if item_data:
                    await session.set(f"job_title:{item.user_id}", item.model_dump_json())
                else:
                    raise HTTPException(status_code=404, detail="Item not found")
            except RedisError as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def delete_item(self, item_id: str) -> None:
        async with self.__session as session:
            try:
                await session.delete(f"job_title:{item_id}")
            except RedisError as e:
                raise HTTPException(status_code=500, detail=str(e))
