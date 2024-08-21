from src.base.job_title.exeptions.interfaces.job_title_error import JobTitleError


class JobTitleNotFoundError(JobTitleError):
    def __init__(self, message: str = "Item not found"):
        self.message = message
