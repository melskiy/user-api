from src.base.user.events.user_event import UserEvent
from src.events.subscriber import Subscriber


class UserCreateEvent(UserEvent):
    def __init__(self, event: Subscriber):
        self.__event = event

    def __call__(self):
        return self.__event
