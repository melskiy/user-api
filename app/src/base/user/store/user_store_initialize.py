from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.db.get_postgre_connection import get_postgres_connection
from src.core.db.get_redis_connection import get_redis_connection
from src.core.ioc import container


class UserStoreInitializer(Initialize):

    async def initialize(self):
        pg_connect = container.resolve(get_postgres_connection)
        redis_connect = container.resolve(get_redis_connection)
        container.register()