from src.core.settings.loader.interfaces.config_loader import ConfigLoader
import yaml


class YamlConfigLoader(ConfigLoader):
    def __init__(self, path: str):
        self.path = path

    def load(self) -> dict:
        with open(self.path, 'r') as file:
            return yaml.safe_load(file)
