from fastapi import FastAPI

from src.base.user.web.exeptions.handlers.handle_user_not_found import handle_user_not_found
from src.base.user.exeptions.user_already_exists_error import UserAlreadyExistsError
from src.base.user.exeptions.user_database_error import UserDatabaseError
from src.base.user.exeptions.user_not_found_error import UserNotFoundError
from src.base.user.web.exeptions.handlers import handle_user_database_error, handle_user_exists
from src.base.user.web.exeptions.handlers.user_error_handler import UserErrorHandler
from src.core.Initializer.interfaces.Initialize import Initialize


class UserExceptionHandlersInitializer(Initialize):

    def __init__(self, app: FastAPI):
        self.__app = app

    async def initialize(self):
        error_handler = UserErrorHandler(self.__app)
        error_handler.register_handler(UserDatabaseError, handle_user_database_error)
        error_handler.register_handler(UserAlreadyExistsError, handle_user_exists)
        error_handler.register_handler(UserNotFoundError, handle_user_not_found)
