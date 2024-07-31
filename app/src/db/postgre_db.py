from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.core.settings import settings
from sqlalchemy.engine import URL


connection_string = URL.create(
    drivername='postgresql+asyncpg',
    username=settings.posgresql_login,
    password=settings.posgresql_password,
    host=settings.posgresql_base_host,
    port=settings.posgresql_base_port,
    database=settings.posgresql_base_name,
)


engine = create_async_engine(
    connection_string
)

Session = async_sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)
