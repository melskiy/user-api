import uvicorn

from src.core.settings import settings

class WebApp:

    def run(self, *args, **kwargs):
        print('Запуск веб-версии приложения')
        uvicorn.run(
            'src.core.Initializer.app:app',
            host=settings.host,
            port=settings.port,
            reload=True,
            factory = True
        )


