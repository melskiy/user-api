from http.client import HTTPException


class JobTitleNotFoundError(HTTPException):
    def __init__(self, message: str = "Item not found"):
        self.message = message
        super().__init__(self.message)
