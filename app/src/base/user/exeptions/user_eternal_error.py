from src.base.user.exeptions.interface.user_error import UserError


class UserEternalError(UserError):
    def __init__(self, message: str):
        self.message = message
