from sqlalchemy.ext.asyncio import async_sessionmaker

from src.base.user.store.interfaceses.user_repository_interface import UserRepositoryInterface
from src.base.user.store.postgres.user_postgres_database_factory import UserPostgresDatabaseFactory
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.db.postgres.get_postgre_connection_factory import GetPostgresConnectionFactory
from src.core.ioc import container


class UserPostgresDatabaseInitializer(Initialize):

    async def initialize(self):
        settings = container.resolve(async_sessionmaker)
        pg_connect = await GetPostgresConnectionFactory()(settings)
        container.register(UserRepositoryInterface, instanse=lambda: UserPostgresDatabaseFactory()(pg_connect))
