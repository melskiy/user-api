from sqlalchemy.ext.asyncio import async_sessionmaker

from src.base.user.store.postgres.postgres_database import PostgresDatabase


class PostgresDatabaseFactory:

    def __call__(self, session: async_sessionmaker) -> PostgresDatabase:
        return PostgresDatabase(
            session=session,
        )
