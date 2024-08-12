from src.core.Initializer.cli_init import CliInitializer


class ConsoleApp:

    def run(self, *args, **kwargs):
        container = kwargs['container']
        CliInitializer(container).initialize(*args)

