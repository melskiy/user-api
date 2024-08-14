from src.core.Initializer.fast_api_init import FastApiInitializer


class WebApp:
    def __init__(self, *args, **kwargs):
        self.__container = kwargs.get('container')
        self.__settings = kwargs.get('settings')

    def run(self, *args):
        FastApiInitializer(self.__container, self.__settings).initialize()
