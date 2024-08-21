from fastapi import FastAPI


class JobTitleErrorHandler:
    def __init__(self, app: FastAPI):
        self.app = app
        self.handlers = {}

    def register_handler(self, error_type, handler):
        self.handlers[error_type] = handler
        self.app.add_exception_handler(error_type, handler)
