class JobTitleAlreadyExistsError(Exception):
    def __init__(self, message: str = "Email already exists"):
        self.message = message
        super().__init__(self.message)
