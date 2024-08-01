from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.engine import URL
from src.core.settings import settings


connection_string = URL.create(
    drivername="postgresql+asyncpg",
    username=settings.postgresql_login,
    password=settings.postgresql_password,
    host=settings.postgresql_base_host,
    port=settings.postgresql_base_port,
    database=settings.postgresql_base_name,
)


engine = create_async_engine(connection_string)

Session = async_sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)
