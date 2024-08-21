from sqlalchemy.ext.asyncio import async_sessionmaker

from src.base.job_title.store.postgres.job_title_postgres_database import JobTitlePostgresDatabase


class JobTitlePostgresDatabaseFactory:

    def __call__(self, session: async_sessionmaker) -> JobTitlePostgresDatabase:
        return JobTitlePostgresDatabase(
            session=session,
        )
