import redis.asyncio as redis

def Sessional():
    repo = redis.Redis(host = "localhost", port = 6379, decode_responses=True)
    return repo

Session = Sessional()