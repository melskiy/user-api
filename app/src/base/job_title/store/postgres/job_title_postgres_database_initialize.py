from sqlalchemy.ext.asyncio import async_sessionmaker

from src.base.job_title.store.postgres.postgres_database import JobTitlePostgresDatabase
from src.base.job_title.store.postgres.postgres_database_factory import JobTitlePostgresDatabaseFactory
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container


class JobTitlePostgresDatabaseInitializer(Initialize):

    async def initialize(self):
        pg_connect = await container.resolve(async_sessionmaker)
        container.register(JobTitlePostgresDatabase, instance=JobTitlePostgresDatabaseFactory()(pg_connect))
