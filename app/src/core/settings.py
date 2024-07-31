from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    host: str
    port: int
    repository_type: str
    posgresql_login: str
    posgresql_password: str
    posgresql_base_host: str
    posgresql_base_port: int
    posgresql_base_name: str
    redis_host: str
    redis_port: int    

settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
