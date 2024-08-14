import click
import asyncio

from src.core.Initializer.app_init import AppInitializer
from src.core.ioc.ioc import container
from src.services.user.create_user import CreateUserService
from src.services.user.delete_user import DeleteUserService
from src.services.user.get_user import GetUserService
from src.services.user.update_user import UpdateUserService


async def run():

    AppInitializer().initialize()

    @click.group()
    def cli():
        pass

    @cli.command()
    @click.argument('user')
    def update(user, methods_service=container.resolve(UpdateUserService)):
        asyncio.run(methods_service.update(user))

    @cli.command()
    @click.argument('id')
    def get(id, methods_service=container.resolve(GetUserService)):
        asyncio.run(methods_service.get(id))

    @cli.command()
    @click.argument('id')
    def delete(id, methods_service=container.resolve(DeleteUserService)):
        asyncio.run(methods_service.delete(id))

    @cli.command()
    @click.argument('user')
    def create(user, methods_service=container.resolve(CreateUserService)):
        asyncio.run(methods_service.create(user))

    cli()

if __name__ == '__main__':
    asyncio.run(run())
