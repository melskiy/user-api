from pydantic import BaseModel


class PostgresSettings(BaseModel):
    driver: str
    login: str
    password: str
    base_host: str
    base_port: int
    base_name: str

