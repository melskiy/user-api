from src.events.base.event import Event
from src.events.subscriber import Subscriber


class EventManager:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber: Subscriber) -> None:
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber) -> None:
        self._subscribers.remove(subscriber)

    async def notify(self, event: Event) -> None:
        for subscriber in self._subscribers:
            subscriber.update(event)
