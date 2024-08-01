import redis.asyncio as redis
from src.core.settings import settings


def Sessional():
    repo = redis.Redis(
        host=settings.redis_host, port=settings.redis_port, decode_responses=True
    )
    return repo


Session = Sessional()
