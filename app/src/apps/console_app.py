from src.core.Initializer.cli_init import CliInitializer


class ConsoleApp:
    def __init__(self, *args, **kwargs):
        self.__container = kwargs['container']

    def run(self, *args):
        CliInitializer(self.__container).initialize(*args)

