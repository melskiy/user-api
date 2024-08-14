class EventManager:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    async def notify(self, data):
        for subscriber in self._subscribers:
            await subscriber(data)
