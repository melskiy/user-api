
from src.base.job_title.services.job_title_service_initializer import JobTitleServiceInitializer
from src.base.job_title.store.job_title_store_initialize import JobTitleStoreInitializer
from src.base.user.services.user_service_initializer import UserServiceInitializer
from src.base.user.store.user_store_initialize import UserStoreInitializer
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container
from src.core.settings.builder.settings_builder_impl import SettingsBuilderImpl
from src.core.settings.loader.impl.env_config_loader import EnvConfigLoader
from src.core.db.postgres.postgres_settings import PostgresSettings
from src.core.db.redis.redis_settings import RedisSettings
from src.core.settings.loader.impl.yml_config_loader import YamlConfigLoader
from src.core.settings.models.settings import Settings


class AppInitializer(Initialize):

    async def initialize(self):
        path = 'config.yaml'

        loader = YamlConfigLoader(path)

        settings_builder = SettingsBuilderImpl([loader])

        config_data = settings_builder.build()

        redis_settings = RedisSettings(
            redis_host=config_data.get('REDIS_HOST'),
            redis_port=config_data.get('REDIS_PORT')
        )

        postgres_settings = PostgresSettings(
            driver=config_data.get('POSTGRESQL_DRIVER'),
            login=config_data.get('POSTGRESQL_LOGIN'),
            password=config_data.get('POSTGRESQL_PASSWORD'),
            base_host=config_data.get('POSTGRESQL_BASE_HOST'),
            base_port=config_data.get('POSTGRESQL_BASE_PORT'),
            base_name=config_data.get('POSTGRESQL_BASE_NAME')
        )

        app_settings = Settings(
            host=config_data.get('HOST'),
            port=config_data.get('PORT'),
            repository_type=config_data.get('REPOSITORY_TYPE')
        )

        container.register(Settings, instance=app_settings)
        store_type = app_settings.repository_type

        store_initializers = {
            'postgresql': lambda: container.register(
                PostgresSettings,
                instance=
                postgres_settings
            ),
            'redis': lambda: container.register(
                RedisSettings,
                instance=
                redis_settings
            )
        }

        store_initializers.get(store_type)()
        await UserStoreInitializer().initialize()
        await JobTitleStoreInitializer().initialize()
        await JobTitleServiceInitializer().initialize()
        await UserServiceInitializer().initialize()
