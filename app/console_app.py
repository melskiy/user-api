import asyncio
import sys

from src.core.Initializer.app_init import AppInitializer
from src.core.Initializer.cli_init import CliInitializer
from src.core.ioc import container
import asyncclick as click


async def run(*args) -> None:
    await AppInitializer().initialize()
    await CliInitializer().initialize(*args)


if __name__ == '__main__':
    asyncio.run(run(sys.argv))
    cli = container.resolve(click)
    asyncio.run(cli())
