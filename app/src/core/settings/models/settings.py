from pydantic import BaseModel


class Settings(BaseModel):
    host: str
    port: int
    repository_type: str
