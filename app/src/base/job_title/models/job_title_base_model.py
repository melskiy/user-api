from pydantic import BaseModel


class JobTitleBaseModel(BaseModel):
    id: str
    name: str
