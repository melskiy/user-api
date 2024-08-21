from src.events.base.event import Event


class Subscriber:
    async def update(self, event: Event):
        raise NotImplementedError
