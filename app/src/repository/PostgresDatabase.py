from src.repository.Interfaceses.RepositoryInterface import RepositoryInterface
from db.postgre_db import Session
from src.models.user import User
from src.models.UserDB import UserDB

class PostgresDatabase(RepositoryInterface):
    def __init__(self):
        pass
    async def create_item(self,user: User):
        async with Session() as session:
            db_user = UserDB(**user)
            session.add(db_user)
            await session.commit()
            
    async def read_item(self, user_id: str) -> UserDB:
        async with Session() as session:
            db_user = await session.get(UserDB, user_id)
            return db_user

    async def update_item(self, user: User):
        async with Session() as session:
            db_user = await session.get(UserDB, user.user_id)
            if db_user:
                for item in user.__dict__:
                    print(user.__dict__[item])
                    setattr(db_user, item, user.__dict__[item])
                await session.commit()

    async def delete_item(self, user_id: str):
        async with Session() as session:
            db_user = await session.get(UserDB, user_id)
            if db_user:
                session.delete(db_user)
                await session.commit()