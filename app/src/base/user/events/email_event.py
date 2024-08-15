from src.events.subscriber import Subscriber


class EmailSubscriber(Subscriber):
    async def update(self):
        print("Отправлено на почту")
