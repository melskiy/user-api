import os
from dotenv import load_dotenv

from src.core.settings.loader.interfaces.config_loader import ConfigLoader


class EnvConfigLoader(ConfigLoader):
    def __init__(self, path: str):
        self.path = path

    def load(self) -> dict:
        load_dotenv(self.path)
        config = {}

        for key, value in os.environ.items():
            config[key] = value

        return config
