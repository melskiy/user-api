from src.base.job_title.cli.job_title_cli_initializer import JobTitleCliInitializer
from src.core.Initializer.interfaces.Initialize import Initialize
from src.core.ioc import container
import asyncclick as click


class CliInitializer(Initialize):
    async def initialize(self, *args):

        @click.group()
        async def cli():
            pass

        container.register(click, instance=cli)
        await JobTitleCliInitializer().initialize()
