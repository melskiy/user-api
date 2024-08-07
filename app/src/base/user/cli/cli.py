import click
import asyncio
import json
from src.base.user.models.user_base_model import UserBaseModel
from src.repository.utils.get_repository import get_repository
from src.services.user.create_user import CreateUserService
from src.services.user.delete_user import DeleteUserService
from src.services.user.get_user import GetUserService
from src.services.user.update_user import UpdateUserService


@click.group()
def cli():
    pass

@cli.command()
@click.argument('user')
def update(user):
    asyncio.run(_update(user))

async def _update(user):
    methods_service = UpdateUserService()
    repo = get_repository()
    user = UserBaseModel.model_validate_json(user)
    result = await methods_service.update(repo, user)
    click.echo(result)

@cli.command()
@click.argument('id')
def get(id):
    asyncio.run(_get(id))

async def _get(id):
    methods_service = GetUserService()
    repo = get_repository()
    user = await methods_service.get(repo, id)
    click.echo(user)

@cli.command()
@click.argument('id')
def delete(id):
    asyncio.run(_delete(id))

async def _delete(id):
    methods_service = DeleteUserService()
    repo = get_repository()
    result = await methods_service.delete(repo, id)
    click.echo(result)

@cli.command()
@click.argument('user')
def create(user):
    asyncio.run(_create(user))

async def _create(user):
    methods_service = CreateUserService()
    repo = get_repository()
    user = UserBaseModel.model_validate_json(user)
    result = await methods_service.create(repo, user)
    click.echo(result)
