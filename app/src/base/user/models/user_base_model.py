from pydantic import BaseModel

class UserBaseModel(BaseModel):
    user_id: str
    name: str
    surname: str
    patronymic: str