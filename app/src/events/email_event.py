from src.events.subscriber import Subscriber


class EmailEvent(Subscriber):
    async def update(self):
        print("Отправлено на почту")