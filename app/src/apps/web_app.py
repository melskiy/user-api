import uvicorn
from src.core.settings import settings


class WebApp:

    def run(self, *args):
        print('Запуск веб-версии приложения')
        uvicorn.run(
            'src.apps.settings.app:app',
            host=settings.host,
            port=settings.port,
            reload=True,
        )
