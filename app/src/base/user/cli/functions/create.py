import click
from src.base.user.models.user_base_model import UserBaseModel
from src.services.user.create_user import CreateUserService


async def create_cli(user: str, methods_service: CreateUserService):
    user = UserBaseModel.model_validate_json(user)
    result = await methods_service.create(user)
    click.echo(result)
