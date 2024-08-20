from src.base.user.exeptions.interface.user_error import UserError


class UserNotFoundError(UserError):
    def __init__(self, message: str = "Item not found"):
        self.message = message
