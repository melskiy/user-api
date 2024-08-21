from fastapi import FastAPI


class UserErrorHandler:
    def __init__(self, app: FastAPI):
        self.app = app
        self.handlers = {}

    def register_handler(self, error_type, handler):
        self.handlers[error_type] = handler
        self.app.exception_handler(error_type)(handler)
