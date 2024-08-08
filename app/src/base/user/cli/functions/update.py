import click

from src.base.user.models.user_base_model import UserBaseModel
from src.services.user.update_user import UpdateUserService


async def update_cli(user):
    methods_service = UpdateUserService()
    user = UserBaseModel.model_validate_json(user)
    result = await methods_service.update(user)
    click.echo(result)
