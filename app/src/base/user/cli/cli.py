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
def update(user):
    asyncio.run(update_cli(user))


@cli.command()
@click.argument('id', nargs=-1)
def get(id):
    asyncio.run(get_cli(id))


@cli.command()
@click.argument('id')
def delete(id):
    asyncio.run(delete_cli(id))


@cli.command()
@click.argument('user')
def create(user):
    asyncio.run(create_cli(user))
