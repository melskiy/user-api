from sqlalchemy.ext.asyncio import async_sessionmaker

from src.base.job_title.exeptions.job_title_database_error import JobTitleDatabaseError
from src.base.job_title.exeptions.job_title_not_found_error import JobTitleNotFoundError
from src.base.job_title.store.adapters.job_title_adapter import job_title_adapter
from src.base.job_title.store.adapters import job_title_db_adapter
from src.base.job_title.models.job_title_db import JobTitleDB
from src.base.job_title.store.interfaceses.repository_interface import JobTitleRepositoryInterface

from src.base.job_title.models.job_title_base_model import JobTitleBaseModel


class JobTitlePostgresDatabase(JobTitleRepositoryInterface):
    def __init__(self, session: async_sessionmaker):
        self.__session = session

    async def create_item(self, job_title: JobTitleBaseModel):
        async with self.__session() as session:
            try:
                db_user = job_title_adapter(job_title)
                session.add(db_user)
                await session.commit()
                return job_title
            except Exception as e:
                await session.rollback()
                raise JobTitleDatabaseError(str(e))

    async def read_item(self, user_id: str) -> JobTitleBaseModel:
        async with self.__session() as session:
            try:
                db_user = await session.get(JobTitleDB, user_id)
                if not db_user:
                    raise JobTitleNotFoundError(f"Job title with ID {user_id} not found.")
                user = job_title_db_adapter(db_user)
                return user
            except Exception as e:
                raise JobTitleDatabaseError(str(e))

    async def update_item(self, user: JobTitleBaseModel):
        async with self.__session() as session:
            try:
                db_user = await session.get(JobTitleDB, user.user_id)
                if db_user:
                    for item in user.__dict__:
                        setattr(db_user, item, user.__dict__[item])
                    await session.commit()
                else:
                    raise JobTitleNotFoundError(f"Job title with ID {user.user_id} not found.")
            except Exception as e:
                await session.rollback()
                raise JobTitleDatabaseError(str(e))

    async def delete_item(self, user_id: str):
        async with self.__session() as session:
            try:
                db_user = await session.get(JobTitleDB, user_id)
                if db_user:
                    await session.delete(db_user)
                    await session.commit()
                else:
                    raise JobTitleNotFoundError(f"Job title with ID {user_id} not found.")
            except Exception as e:
                await session.rollback()
                raise JobTitleDatabaseError(str(e))
