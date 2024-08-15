import asyncio

import asyncclick as click

from src.core.Initializer.app_init import AppInitializer
from src.core.ioc import container
from src.services.job_title.create_job_title import CreateJobTitleService
from src.services.job_title.delete_job_title import DeleteJobTitleService
from src.services.job_title.get_job_title import GetJobTitleService
from src.services.job_title.update_job_title import UpdateJobTitleService
from src.services.user.create_user import CreateUserService
from src.services.user.delete_user import DeleteUserService
from src.services.user.get_user import GetUserService
from src.services.user.update_user import UpdateUserService

app_initializer = AppInitializer()


@click.group()
async def cli():
    pass


@cli.command()
@click.argument('user')
async def update(user, methods_service=container.resolve(UpdateJobTitleService)):
    await methods_service.update(user)


@cli.command()
@click.argument('id')
async def get(id, methods_service=container.resolve(GetJobTitleService)):
    await methods_service.get(id)


@cli.command()
@click.argument('id')
async def delete(id, methods_service=container.resolve(DeleteJobTitleService)):
    await methods_service.delete(id)


@cli.command()
@click.argument('user')
async def create(user, methods_service=container.resolve(CreateJobTitleService)):
    await methods_service.create(user)


async def run() -> None:
    await AppInitializer().initialize()
    cli()


if __name__ == '__main__':
    asyncio.run(run())
