from fastapi import HTTPException
from typing import Optional
from src.models.user import User
from src.repository.Interfaceses.repository_interface import RepositoryInterface
from src.db.redis_db import Session


class RedisDatabase(RepositoryInterface):
    def __init__(self):
        pass

    async def create_item(self, item: User):
        async with Session as session:
            await session.set(f"user:{item.user_id}", item.model_dump_json())

    async def read_item(self, item_id: str) -> Optional[User]:
        async with Session as session:
            item_data = await session.get(f"user:{item_id}")
            if item_data:
                return User.model_validate_json(item_data)
            raise HTTPException(status_code=404, detail="Item not found")

    async def update_item(self, item: User):
        async with Session as session:
            item_data = await session.get(f"user:{item.user_id}")
            if item_data:
                await session.set(f"user:{item.user_id}", item.model_dump_json())
            else:
                raise HTTPException(status_code=404, detail="Item not found")

    async def delete_item(self, item_id: str):
        async with Session as session:
            await session.delete(f"user:{item_id}")
