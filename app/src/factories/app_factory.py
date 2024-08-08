class AppFactory:
    _apps = {}

    @classmethod
    def register(cls, key, app_class):
        cls._apps[key] = app_class

    @classmethod
    def create(cls, key, *args, **kwargs):
        app_class = cls._apps.get(key)
        if app_class:
            return app_class(*args, **kwargs)
        else:
            raise ValueError(f"Неверный ключ приложения: {key}")