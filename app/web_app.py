import asyncio

import uvicorn
from fastapi import FastAPI

from src.core.Initializer.app_init import AppInitializer
from src.core.Initializer.web_init import WebInitializer
from src.core.ioc import container
from src.core.settings.settings import Settings


async def run() -> None:
    await AppInitializer().initialize()
    await WebInitializer().initialize()

if __name__ == '__main__':
    asyncio.run(run())
    app = container.resolve(FastAPI)
    settings = container.resolve(Settings)

    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port,
    )
