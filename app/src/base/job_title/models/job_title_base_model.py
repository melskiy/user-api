from pydantic import BaseModel


class JobTitleBaseModel(BaseModel):
    job_title_id: str
    job_title_name: str
