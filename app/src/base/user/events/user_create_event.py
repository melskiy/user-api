from src.events.subscriber import Subscriber


class UserCreateSubscriber(Subscriber):
    async def update(self):
        print("Отправлено на почту")
