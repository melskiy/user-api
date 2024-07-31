from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    name: str
    surname: str
    patronymic: str