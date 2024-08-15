from sqlalchemy.ext.asyncio import async_sessionmaker

from src.base.job_title.models.adapters.job_title_adapter import job_title_adapter
from src.base.job_title.models.adapters.job_title_db_adapter import job_title_db_adapter
from src.base.job_title.models.job_title_db import JobTitleDB
from src.base.job_title.store.interfaceses.repository_interface import RepositoryInterface

from src.base.job_title.models.job_title_base_model import JobTitleBaseModel
from sqlalchemy.exc import SQLAlchemyError, NoResultFound
from fastapi import HTTPException


class PostgresDatabase(RepositoryInterface):
    def __init__(self, session: async_sessionmaker):
        self.__session = session

    async def create_item(self, user: JobTitleBaseModel):
        async with self.__session() as session:
            try:
                db_user = job_title_db_adapter(user)
                session.add(db_user)
                await session.commit()
                return user
            except SQLAlchemyError as e:
                await session.rollback()
                raise HTTPException(status_code=500, detail=str(e))

    async def read_item(self, user_id: str) -> JobTitleBaseModel:
        async with self.__session() as session:
            try:
                db_user= await session.get(JobTitleDB, user_id)
                if not db_user:
                    raise NoResultFound(f"UserBaseModel with id {user_id} not found")
                user = job_title_adapter(db_user)
                return user
            except NoResultFound as e:
                raise HTTPException(status_code=404, detail=str(e))
            except SQLAlchemyError as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def update_item(self, user: JobTitleBaseModel):
        async with self.__session() as session:
            try:
                db_user = await session.get(JobTitleDB, user.user_id)
                if db_user:
                    for item in user.__dict__:
                        setattr(db_user, item, user.__dict__[item])
                    await session.commit()
                else:
                    raise NoResultFound(f"UserBaseModel with id {user.user_id} not found")
            except NoResultFound as e:
                raise HTTPException(status_code=404, detail=str(e))
            except SQLAlchemyError as e:
                await session.rollback()
                raise HTTPException(status_code=500, detail=str(e))

    async def delete_item(self, user_id: str):
        async with self.__session() as session:
            try:
                db_user = await session.get(JobTitleDB, user_id)
                if db_user:
                    await session.delete(db_user)
                    await session.commit()
                else:
                    raise NoResultFound(f"UserBaseModel with id {user_id} not found")
            except NoResultFound as e:
                raise HTTPException(status_code=404, detail=str(e))
            except SQLAlchemyError as e:
                await session.rollback()
                raise HTTPException(status_code=500, detail=str(e))
