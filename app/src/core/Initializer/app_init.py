from dotenv import load_dotenv

from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.db.get_postgre_connection import get_postgres_connection
from src.core.db.get_redis_connection import get_redis_connection
from src.core.ioc import container
from src.core.settings.postgres_settings import PostgresSettings
from src.core.settings.redis_settings import RedisSettings
from src.core.settings.settings import Settings
from src.base.user.events.email_event import EmailSubscriber
from src.events.event_manager_factory import EventManagerFactory

from src.events.event_manger import EventManager
from src.repository.postgres.postgres_database_factory import PostgresDatabaseFactory
from src.repository.redis.redis_database_factory import RedisDatabaseFactory
from src.services.job_title.create_job_title import CreateJobTitleService
from src.services.job_title.delete_job_title import DeleteJobTitleService
from src.services.job_title.get_job_title import GetJobTitleService
from src.services.job_title.update_job_title import UpdateJobTitleService
from src.services.user.create_user import CreateUserService
from src.services.user.delete_user import DeleteUserService
from src.services.user.get_user import GetUserService
from src.services.user.update_user import UpdateUserService


class AppInitializer(Initialize):

    async def initialize(self):
        settings = Settings(
            _env_file=".env",
            _env_file_encoding="utf-8",
        )
        load_dotenv()
        postgres_settings = PostgresSettings()
        redis_settings = RedisSettings()
        pg_connect = await get_postgres_connection(postgres_settings)
        redis_connect = await get_redis_connection(redis_settings)

        container.register('postgresql', instance=PostgresDatabaseFactory()(pg_connect))
        container.register('redis', instance=RedisDatabaseFactory()(redis_connect))

        manager = EventManagerFactory()()

        manager.subscribe(EmailSubscriber())
        container.register(EventManager, instance=manager)

        repo = container.resolve(settings.repository_type)

        container.register(CreateUserService, instance=CreateUserService(repo, container.resolve(EventManager)))
        container.register(UpdateUserService, instance=UpdateUserService(repo))
        container.register(GetUserService, instance=GetUserService(repo))
        container.register(DeleteUserService, instance=DeleteUserService(repo))

        container.register(CreateJobTitleService, instance=CreateJobTitleService(repo))
        container.register(UpdateJobTitleService, instance=UpdateJobTitleService(repo))
        container.register(GetJobTitleService, instance=UpdateJobTitleService(repo))
        container.register(DeleteJobTitleService, instance=UpdateJobTitleService(repo))
