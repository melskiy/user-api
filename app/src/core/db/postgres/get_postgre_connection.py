from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.core.db.postgres.postgres_settings import PostgresSettings


async def get_postgres_connection(settings: PostgresSettings) -> async_sessionmaker:

    connection_string = URL.create(
        drivername=settings.driver,
        username=settings.login,
        password=settings.password,
        host=settings.base_host,
        port=settings.base_port,
        database=settings.base_name,
    )

    engine = create_async_engine(connection_string)

    session = async_sessionmaker(
        engine,
        autocommit=False,
        autoflush=False,
    )
    return session
