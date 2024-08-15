from typing import Any, Coroutine

from sqlalchemy.ext.asyncio import async_sessionmaker

from src.core.db.get_postgre_connection import get_postgres_connection
from src.core.settings.postgres_settings import PostgresSettings


class GetPostgresConnectionFactory:

    def __call__(self, settings: PostgresSettings) -> Coroutine[Any, Any, async_sessionmaker]:
        return get_postgres_connection(
            settings=settings,
        )