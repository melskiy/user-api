import os
from dotenv import load_dotenv


class EnvConfigLoader:
    def __init__(self, path: str):
        self.path = path

    def load(self) -> dict:
        load_dotenv(self.path)
        config = {}

        for key, value in os.environ.items():
            config[key] = value

        return config
