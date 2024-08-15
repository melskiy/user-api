import asyncio

import asyncclick as click

from src.core.Initializer.app_init import AppInitializer
from src.core.ioc import container
from src.services.user.create_user import CreateUserService
from src.services.user.delete_user import DeleteUserService
from src.services.user.get_user import GetUserService
from src.services.user.update_user import UpdateUserService

app_initializer = AppInitializer()


async def run() -> None:
    await AppInitializer().initialize()
    cli()


@click.group()
async def cli():
    pass


@cli.command()
@click.argument('user')
async def update(user, methods_service=container.resolve(UpdateUserService)):
    await methods_service.update(user)


@cli.command()
@click.argument('id')
async def get(id, methods_service=container.resolve(GetUserService)):
    await methods_service.get(id)


@cli.command()
@click.argument('id')
async def delete(id, methods_service=container.resolve(DeleteUserService)):
    await methods_service.delete(id)


@cli.command()
@click.argument('user')
async def create(user, methods_service=container.resolve(CreateUserService)):
    await methods_service.create(user)


if __name__ == '__main__':
    asyncio.run(run())
