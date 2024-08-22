from pydantic import BaseModel


class RedisSettings(BaseModel):
    redis_host: str
    redis_port: int
