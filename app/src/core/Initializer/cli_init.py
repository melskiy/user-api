from rodi import Container
from src.core.Initializer.interfaces.Initialize import Initialize
import click
import asyncio
from src.base.user.cli.functions.create import create_cli
from src.base.user.cli.functions.delete import delete_cli
from src.base.user.cli.functions.get import get_cli
from src.base.user.cli.functions.update import update_cli
from src.services.user.create_user import CreateUserService
from src.services.user.delete_user import DeleteUserService
from src.services.user.get_user import GetUserService
from src.services.user.update_user import UpdateUserService


class CliInitializer(Initialize):

    def __init__(self, __container: Container):
        self.__container = __container

    def initialize(self, *args):
        container = self.__container

        @click.group()
        def cli():
            pass

        @cli.command()
        @click.argument('user')
        def update(user, methods_service=container.resolve(UpdateUserService)):
            asyncio.run(update_cli(user, methods_service))

        @cli.command()
        @click.argument('id', nargs=-1)
        def get(id, methods_service=container.resolve(GetUserService)):
            asyncio.run(get_cli(id, methods_service))

        @cli.command()
        @click.argument('id')
        def delete(id, methods_service=container.resolve(DeleteUserService)):
            asyncio.run(delete_cli(id, methods_service))

        @cli.command()
        @click.argument('user')
        def create(user, methods_service=container.resolve(CreateUserService)):
            asyncio.run(create_cli(user, methods_service))

        cli(*args)
