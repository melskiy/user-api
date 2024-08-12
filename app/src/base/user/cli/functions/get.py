import click

from src.services.user.get_user import GetUserService


async def get_cli(id, methods_service: GetUserService):
    user = await methods_service.get(id)
    click.echo(user)
