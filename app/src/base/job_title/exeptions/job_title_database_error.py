from src.base.job_title.exeptions.interfaces.job_title_error import JobTitleError


class JobTitleDatabaseError(JobTitleError):
    def __init__(self, message: str):
        self.message = message
