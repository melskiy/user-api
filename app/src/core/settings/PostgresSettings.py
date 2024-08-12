from pydantic_settings import BaseSettings


class PostgresSettings(BaseSettings):
    postgresql_driver: str
    postgresql_login: str
    postgresql_password: str
    postgresql_base_host: str
    postgresql_base_port: int
    postgresql_base_name: str


