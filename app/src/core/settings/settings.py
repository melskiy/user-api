from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    host: str
    port: int
    repository_type: str
