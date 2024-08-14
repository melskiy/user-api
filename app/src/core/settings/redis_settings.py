from pydantic_settings import BaseSettings


class RedisSettings(BaseSettings):
    redis_host: str
    redis_port: str
