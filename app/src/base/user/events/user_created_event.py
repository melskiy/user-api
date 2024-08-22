from src.base.user.models.user_base_model import UserBaseModel
from src.events.base.event import Event


class UserCreatedEvent(Event):
    user: UserBaseModel
