from src.base.user.exeptions.interface.user_error import UserError


class UserDatabaseError(UserError):
    def __init__(self, message: str):
        self.message = message
