from redis.asyncio import Redis
from src.base.user.exeptions.user_already_exists_error import UserAlreadyExistsError
from src.base.user.exeptions.user_database_error import UserDatabaseError
from src.base.user.exeptions.user_not_found_error import UserNotFoundError
from src.base.user.models.user_base_model import UserBaseModel
from src.base.user.store.interfaceses.user_repository_interface import UserRepositoryInterface


class UserRedisDatabase(UserRepositoryInterface):
    def __init__(self, session: Redis):
        self.__session = session

    async def create_item(self, item: UserBaseModel) -> None:
        async with self.__session as session:
            try:
                existing_user = await session.get(f"user:email:{item.email}")
                if existing_user:
                    raise UserAlreadyExistsError()
                await session.set(f"user:email:{item.email}", item.user_id)
                await session.set(f"user:{item.user_id}", item.model_dump_json())
            except Exception as e:
                raise UserDatabaseError(str(e))

    async def read_item(self, item_id: str) -> UserBaseModel:
        async with self.__session as session:
            try:
                item_data = await session.get(f"user:{item_id}")
                if item_data:
                    return UserBaseModel.model_validate_json(item_data)
                raise UserNotFoundError(f"User with ID {item_id} not found.")
            except Exception as e:
                raise UserDatabaseError(str(e)) from e

    async def update_item(self, item: UserBaseModel) -> None:
        async with self.__session as session:
            try:
                item_data = await session.get(f"user:{item.user_id}")
                if item_data:
                    await session.set(f"user:{item.user_id}", item.model_dump_json())
                else:
                    raise UserNotFoundError()
            except Exception as e:
                raise UserDatabaseError(str(e))

    async def delete_item(self, item_id: str) -> None:
        async with self.__session as session:
            try:
                await session.delete(f"user:{item_id}")
            except Exception as e:
                raise UserDatabaseError(str(e))
