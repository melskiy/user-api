from sqlalchemy.ext.asyncio import async_sessionmaker

from src.base.user.store.postgres.user_postgres_database import UserPostgresDatabase
from src.base.user.store.postgres.user_postgres_database_factory import UserPostgresDatabaseFactory
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container


class UserPostgresDatabaseInitializer(Initialize):

    async def initialize(self):
        pg_connect = container.resolve(async_sessionmaker)
        container.register(UserPostgresDatabase, instance=UserPostgresDatabaseFactory()(pg_connect))
