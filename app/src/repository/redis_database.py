from fastapi import HTTPException
from typing import Optional
from src.models.user import User
from src.repository.Interfaceses.repository_interface import RepositoryInterface
from src.db.redis_db import Session
from redis.exceptions import RedisError


class RedisDatabase(RepositoryInterface):
    def __init__(self):
        pass

    async def create_item(self, item: User) -> User:
        async with Session as session:
            try:
                await session.set(f"user:{item.user_id}", item.model_dump_json())
                return item
            except RedisError as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def read_item(self, item_id: str) -> Optional[User]:
        async with Session as session:
            try:
                item_data = await session.get(f"user:{item_id}")
                if item_data:
                    return User.model_validate_json(item_data)
                raise HTTPException(status_code=404, detail="Item not found")
            except RedisError as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def update_item(self, item: User) -> None:
        async with Session as session:
            try:
                item_data = await session.get(f"user:{item.user_id}")
                if item_data:
                    await session.set(f"user:{item.user_id}", item.model_dump_json())
                else:
                    raise HTTPException(status_code=404, detail="Item not found")
            except RedisError as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def delete_item(self, item_id: str) -> None:
        async with Session as session:
            try:
                await session.delete(f"user:{item_id}")
            except RedisError as e:
                raise HTTPException(status_code=500, detail=str(e))
