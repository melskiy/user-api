from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    host: str
    port: int
    repository_type: str
    postgresql_login: str
    postgresql_password: str
    postgresql_base_host: str
    postgresql_base_port: int
    postgresql_base_name: str
    redis_host: str
    redis_port: int


settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8",
)
