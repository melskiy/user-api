import asyncio

import asyncclick as click

from src.core.Initializer.app_init import AppInitializer
from src.core.Initializer.cli_init import CliInitializer
from src.core.ioc import container
from src.services.job_title.create_job_title import CreateJobTitleService
from src.services.job_title.delete_job_title import DeleteJobTitleService
from src.services.job_title.get_job_title import GetJobTitleService
from src.services.job_title.update_job_title import UpdateJobTitleService

app_initializer = AppInitializer()
cli_initializer = CliInitializer()

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
    await CliInitializer().initialize()
    cli()


if __name__ == '__main__':
    asyncio.run(run())
