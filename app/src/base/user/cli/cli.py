import click
import asyncio
from src.base.user.cli.functions.create import create_cli
from src.base.user.cli.functions.delete import delete_cli
from src.base.user.cli.functions.get import get_cli
from src.base.user.cli.functions.update import update_cli


@click.group()
def cli():
    pass


@cli.command()
@click.argument('user')
def update(user, methods_service):
    asyncio.run(update_cli(user, methods_service))


@cli.command()
@click.argument('id', nargs=-1)
def get(id, methods_service):
    asyncio.run(get_cli(id, methods_service))


@cli.command()
@click.argument('id')
def delete(id, methods_service):
    asyncio.run(delete_cli(id,methods_service))


@cli.command()
@click.argument('user')
def create(user, methods_service):
    asyncio.run(create_cli(user, methods_service))
