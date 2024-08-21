from src.base.user.exeptions.interface.user_error import UserError


class UserAlreadyExistsError(UserError):
    def __init__(self, message: str = "Email already exists"):
        self.message = message
