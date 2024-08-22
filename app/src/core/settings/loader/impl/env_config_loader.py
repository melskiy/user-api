import os
from dotenv import load_dotenv

from src.core.settings.loader.interfaces.config_loader import ConfigLoader


class EnvConfigLoader(ConfigLoader):
    def __init__(self, path: str):
        self.path = path

    def load(self) -> dict:
        load_dotenv(self.path)
        return {
            "HOST": os.getenv('HOST', 'localhost'),
            "PORT": int(os.getenv('PORT', 11000)),
            "REPOSITORY_TYPE": os.getenv('REPOSITORY_TYPE', 'postgresql'),
            "POSTGRESQL_DRIVER": os.getenv('POSTGRESQL_DRIVER', ''),
            "POSTGRESQL_LOGIN": os.getenv('POSTGRESQL_LOGIN', ''),
            "POSTGRESQL_PASSWORD": os.getenv('POSTGRESQL_PASSWORD', ''),
            "POSTGRESQL_BASE_HOST": os.getenv('POSTGRESQL_BASE_HOST', ''),
            "POSTGRESQL_BASE_PORT": int(os.getenv('POSTGRESQL_BASE_PORT', 5432)),
            "POSTGRESQL_BASE_NAME": os.getenv('POSTGRESQL_BASE_NAME', ''),
            "REDIS_HOST": os.getenv('REDIS_HOST', ''),
            "REDIS_PORT": int(os.getenv('REDIS_PORT', 6379))
        }
