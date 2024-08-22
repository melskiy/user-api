from src.base.job_title.store.interfaceses.job_title_repository_interface import JobTitleRepositoryInterface
from src.base.job_title.store.postgres.job_title_postgres_database_factory import JobTitlePostgresDatabaseFactory
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.db.postgres.get_postgre_connection_factory import GetPostgresConnectionFactory
from src.core.ioc import container
from src.core.db.postgres.postgres_settings import PostgresSettings


class JobTitlePostgresDatabaseInitializer(Initialize):

    async def initialize(self):
        settings = container.resolve(PostgresSettings)
        pg_connect = await GetPostgresConnectionFactory()(settings)
        container.register(JobTitleRepositoryInterface, instance=lambda: JobTitlePostgresDatabaseFactory()(pg_connect))
