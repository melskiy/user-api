from pydantic_settings import BaseSettings
from src.repository.InMemoryDatabase import InMemoryDatabase
from src.repository.PostgresDatabase import PostgresDatabase
from src.factories.RepositoryFactory import RepositoryFactory

class Settings(BaseSettings):
    host: str
    port: int
    repository_type: str
    login: str
    password: str
    base_host: str
    base_port: int
    base_name: str

settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)

RepositoryFactory.register('memory', InMemoryDatabase)
RepositoryFactory.register('postgresql', PostgresDatabase)
