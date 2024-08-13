from src.core.Initializer.cli_init import CliInitializer


class ConsoleApp:
    def __init__(self, *args, **kwargs):
        self.__container = kwargs['container']
        self.args = args

    def run(self):
        CliInitializer(self.__container).initialize(self.args)

