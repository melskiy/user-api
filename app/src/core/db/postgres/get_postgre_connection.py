from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.core.settings.postgres_settings import PostgresSettings


async def get_postgres_connection(settings: PostgresSettings) -> async_sessionmaker:

    connection_string = URL.create(
        drivername=settings.postgresql_driver,
        username=settings.postgresql_login,
        password=settings.postgresql_password,
        host=settings.postgresql_base_host,
        port=settings.postgresql_base_port,
        database=settings.postgresql_base_name,
    )

    engine = create_async_engine(connection_string)

    session = async_sessionmaker(
        engine,
        autocommit=False,
        autoflush=False,
    )
    return session
