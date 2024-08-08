from src.base.user.cli.cli import cli


class ConsoleApp:

    def run(self, *args):
        print('Запуск консольной версии приложения')
        cli(*args)
