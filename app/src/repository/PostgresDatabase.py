from src.repository.Interfaceses.RepositoryInterface import RepositoryInterface
from src.db.db import Session
from src.models.user import User
from src.models.UserDB import UserDB

class PostgresDatabase(RepositoryInterface):
    def __init__(self):
        pass
    async def create_item(self,user: User):
        async with Session() as session:
            db_user = UserDB(userid=user.user_id, lastname=user.name, firstname=user.surname, patronymic=user.patronymic)
            session.add(db_user)
            await session.commit()
            
    async def read_item(self):
        pass

    async def update_item(self):
        pass

    async def delete_item(self):
        pass
