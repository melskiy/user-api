from src.base.user.events.UserEvent import UserEvent
from src.events.subscriber import Subscriber


class UserCreateEvent(UserEvent):
    def __init__(self, event: Subscriber):
        self.__event = event

    def __call__(self):
        self.__event.update()
