from src.events.subscriber import Subscriber


class EmailEvent(Subscriber):
    async def update(self) -> None:
        print("Отправлено на почту")
