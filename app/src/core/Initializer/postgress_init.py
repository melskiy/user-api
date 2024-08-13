from typing import Type

from rodi import Container
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv

from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.settings.postgres_settings import PostgresSettings


class PostgresInitializer(Initialize):

    def __init__(self, __container: Container):
        self.__container = __container

    def initialize(self):
        container = self.__container
        load_dotenv()
        postgres_settings = PostgresSettings()

        connection_string = URL.create(
            drivername=postgres_settings.postgresql_driver,
            username=postgres_settings.postgresql_login,
            password=postgres_settings.postgresql_password,
            host=postgres_settings.postgresql_base_host,
            port=postgres_settings.postgresql_base_port,
            database=postgres_settings.postgresql_base_name,
        )

        engine = create_async_engine(connection_string)

        session = async_sessionmaker(
            engine,
            autocommit=False,
            autoflush=False,
        )

        container.register(Type[async_sessionmaker], instance=session)



