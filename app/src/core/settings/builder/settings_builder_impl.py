from typing import Any

from src.core.settings.loader.interfaces.config_loader import ConfigLoader


class SettingsBuilderImpl:

    def __init__(self, loaders: list[ConfigLoader]):
        self.loaders = loaders

    def build(self) -> dict[Any, Any]:
        config_data = {}
        for loader in self.loaders:
            config_data.update(loader.load())

        return config_data
