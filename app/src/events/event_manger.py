from src.events.subscriber import Subscriber


class EventManager:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber: Subscriber) -> None:
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber) -> None:
        self._subscribers.remove(subscriber)

    async def notify(self) -> None:
        for subscriber in self._subscribers:
            await subscriber.update()
