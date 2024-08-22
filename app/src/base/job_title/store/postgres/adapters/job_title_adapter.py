from src.base.job_title.models.job_title_base_model import JobTitleBaseModel
from src.base.job_title.store.postgres.models.job_title_db import JobTitleDB


def job_title_adapter(job_title: JobTitleBaseModel) -> JobTitleDB:
    job_title = JobTitleDB(
        job_title_id=job_title.id,
        job_title_name=job_title.name
    )
    return job_title
