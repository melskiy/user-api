from fastapi import APIRouter

from src.core.Initializer.app import FastApiInitializer
from src.core.Initializer.web_init import WebInitializer


class WebApp:

    def run(self, *args, **kwargs):
        container = kwargs['container']
        router = APIRouter()
        WebInitializer(container, router).initialize()
        FastApiInitializer(container).initialize()

