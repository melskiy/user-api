from typing import Any


class SettingsBuilderImpl:

    def __init__(self, loaders: list):
        self.loaders = loaders

    def build(self) -> dict[Any, Any]:
        config_data = {}
        for loader in self.loaders:
            config_data.update(loader.load())

        return config_data
