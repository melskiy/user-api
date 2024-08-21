from sqlalchemy.ext.asyncio import async_sessionmaker

from src.base.user.store.postgres.user_postgres_database import UserPostgresDatabase


class UserPostgresDatabaseFactory:

    def __call__(self, session: async_sessionmaker) -> UserPostgresDatabase:
        return UserPostgresDatabase(
            session=session,
        )
