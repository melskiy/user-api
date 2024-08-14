
from src.core.Initializer.fast_api_init import FastApiInitializer


class WebApp:
    def __init__(self, *args, **kwargs):
        self.__container = kwargs.get('container')

    def run(self):
        FastApiInitializer(self.__container).initialize()

