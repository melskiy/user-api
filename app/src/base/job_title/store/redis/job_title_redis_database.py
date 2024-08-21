from redis.asyncio import Redis
from src.base.job_title.exeptions.job_title_database_error import JobTitleDatabaseError
from src.base.job_title.exeptions.job_title_not_found_error import JobTitleNotFoundError
from src.base.job_title.models.job_title_base_model import JobTitleBaseModel
from src.base.job_title.store.interfaceses.job_title_repository_interface import JobTitleRepositoryInterface


class JobTitleRedisDatabase(JobTitleRepositoryInterface):
    def __init__(self, session: Redis):
        self.__session = session

    async def create_item(self, item: JobTitleBaseModel) -> None:
        async with self.__session as session:
            try:
                await session.set(f"job_title:{item.id}", item.model_dump_json())
            except Exception as e:
                raise JobTitleDatabaseError(str(e))

    async def read_item(self, item_id: str) -> JobTitleBaseModel:
        async with self.__session as session:
            try:
                item_data = await session.get(f"job_title:{item_id}")
                if item_data:
                    return JobTitleBaseModel.model_validate_json(item_data)
                raise JobTitleNotFoundError(f"Job title with ID {item_id} not found.")
            except Exception as e:
                raise JobTitleDatabaseError(str(e)) from e

    async def update_item(self, item: JobTitleBaseModel) -> None:
        async with self.__session as session:
            try:
                item_data = await session.get(f"job_title:{item.id}")
                if item_data:
                    await session.set(f"job_title:{item.id}", item.model_dump_json())
                else:
                    raise JobTitleNotFoundError(f"Job title with ID {item.id} not found.")
            except Exception as e:
                raise JobTitleDatabaseError(str(e))

    async def delete_item(self, item_id: str) -> None:
        async with self.__session as session:
            try:
                await session.delete(f"job_title:{item_id}")
            except Exception as e:
                raise JobTitleDatabaseError(str(e))
