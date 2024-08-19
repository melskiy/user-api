from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.base.user.exeptions.user_already_exists_error import UserAlreadyExistsError
from src.base.user.exeptions.user_database_error import UserDatabaseError
from src.base.user.exeptions.user_not_found_error import UserNotFoundError
from src.base.user.store.adapters import user_db_adapter
from src.base.user.store.adapters.user_db_adapter import user_adapter
from src.base.user.store.interfaceses.repository_interface import UserRepositoryInterface
from src.base.user.models.user_base_model import UserBaseModel
from src.base.user.models.user_db import UserDB
from sqlalchemy.exc import SQLAlchemyError


class UserPostgresDatabase(UserRepositoryInterface):
    def __init__(self, session: async_sessionmaker):
        self.__session = session

    async def create_item(self, user: UserBaseModel) -> None:
        async with self.__session() as session:
            try:
                db_user = user_db_adapter(user)
                existing_user = await session.execute(select(UserDB).where(UserDB.email == user.email))
                if existing_user.scalar():
                    raise UserAlreadyExistsError()

                session.add(db_user)
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise UserDatabaseError(str(e))

    async def read_item(self, item_id: str) -> UserBaseModel:
        async with self.__session() as session:
            try:
                db_user = await session.get(UserDB, item_id)
                if not db_user:
                    raise UserNotFoundError()
                user = user_adapter(db_user)
                return user
            except SQLAlchemyError as e:
                raise UserDatabaseError(str(e))

    async def update_item(self, user: UserBaseModel):
        async with self.__session() as session:
            try:
                db_user = await session.get(UserDB, user.user_id)
                if db_user:
                    for item in user.__dict__:
                        setattr(db_user, item, user.__dict__[item])
                    await session.commit()
                else:
                    raise UserNotFoundError()
            except SQLAlchemyError as e:
                await session.rollback()
                raise UserDatabaseError(str(e))

    async def delete_item(self, user_id: str):
        async with self.__session() as session:
            try:
                db_user = await session.get(UserDB, user_id)
                if db_user:
                    await session.delete(db_user)
                    await session.commit()
                else:
                    raise UserNotFoundError()
            except SQLAlchemyError as e:
                await session.rollback()
                raise UserDatabaseError(str(e))
