from src.base.job_title.exeptions.interfaces.job_title_error import JobTitleError


class JobTitleAlreadyExistsError(JobTitleError):
    def __init__(self, message: str = "Email already exists"):
        self.message = message
