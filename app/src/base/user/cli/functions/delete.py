import click
from src.services.user.delete_user import DeleteUserService


async def delete_cli(id, methods_service: DeleteUserService):
    result = await methods_service.delete(id)
    click.echo(result)
