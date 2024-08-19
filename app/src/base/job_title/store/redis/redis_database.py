from typing import Optional

from redis.asyncio import Redis

from src.base.job_title.exeptions.job_title_database_error import JobTitleDatabaseError
from src.base.job_title.exeptions.job_title_not_found_error import JobTitleNotFoundError
from src.base.job_title.models.job_title_base_model import JobTitleBaseModel
from src.base.job_title.store.interfaceses.repository_interface import JobTitleRepositoryInterface
from redis.exceptions import RedisError


class JobTitleRedisDatabase(JobTitleRepositoryInterface):
    def __init__(self, session: Redis):
        self.__session = session

    async def create_item(self, item: JobTitleBaseModel) -> JobTitleBaseModel:
        async with self.__session as session:
            try:
                await session.set(f"job_title:{item.job_title_id}", item.model_dump_json())
                return item
            except RedisError as e:
                raise JobTitleDatabaseError(str(e))

    async def read_item(self, item_id: str) -> Optional[JobTitleBaseModel]:
        async with self.__session as session:
            try:
                item_data = await session.get(f"job_title:{item_id}")
                if item_data:
                    return JobTitleBaseModel.model_validate_json(item_data)
                raise JobTitleNotFoundError(f"Job title with ID {item_id} not found.")
            except RedisError as e:
                raise JobTitleDatabaseError(str(e))

    async def update_item(self, item: JobTitleBaseModel) -> None:
        async with self.__session as session:
            try:
                item_data = await session.get(f"job_title:{item.job_title_id}")
                if item_data:
                    await session.set(f"job_title:{item.job_title_id}", item.model_dump_json())
                else:
                    raise JobTitleNotFoundError(f"Job title with ID {item.job_title_id} not found.")
            except RedisError as e:
                raise JobTitleDatabaseError(str(e))

    async def delete_item(self, item_id: str) -> None:
        async with self.__session as session:
            try:
                await session.delete(f"job_title:{item_id}")
            except RedisError as e:
                raise JobTitleDatabaseError(str(e))
