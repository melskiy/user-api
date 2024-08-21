from src.base.user.events.user_created_event import UserCreatedEvent
from src.events.subscriber import Subscriber


class UserCreateEventHandler(Subscriber):
    def update(self, event: UserCreatedEvent):
        print("send email")
