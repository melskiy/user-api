from src.base.user.models.adapters.user_adapter import user_db_adapter
from src.base.user.models.adapters.user_db_adapter import user_adapter
from src.repository.interfaceses.repository_interface import RepositoryInterface
from src.base.user.models.user_base_model import UserBaseModel
from src.base.user.models.user_db import UserDB
from sqlalchemy.exc import SQLAlchemyError, NoResultFound
from fastapi import HTTPException


class PostgresDatabase(RepositoryInterface):
    def __init__(self, session):
        self.__session = session

    async def create_item(self, user: UserBaseModel):
        async with self.__session() as session:
            try:
                db_user = user_db_adapter(user)
                session.add(db_user)
                await session.commit()
                return user
            except SQLAlchemyError as e:
                await session.rollback()
                raise HTTPException(status_code=500, detail=str(e))

    async def read_item(self, user_id: str) -> UserBaseModel:
        async with self.__session() as session:
            try:
                db_user = await session.get(UserDB, user_id)
                if not db_user:
                    raise NoResultFound(f"UserBaseModel with id {user_id} not found")
                user = user_adapter(db_user)
                return user
            except NoResultFound as e:
                raise HTTPException(status_code=404, detail=str(e))
            except SQLAlchemyError as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def update_item(self, user: UserBaseModel):
        async with self.__session() as session:
            try:
                db_user = await session.get(UserDB, user.user_id)
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
                db_user = await session.get(UserDB, user_id)
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
