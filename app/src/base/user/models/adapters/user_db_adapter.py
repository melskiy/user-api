from src.base.user.models.user_base_model import JobTitleBaseModel
from src.base.user.models.user_db import UserDB


def user_adapter(userdb: UserDB) -> JobTitleBaseModel:
    user = JobTitleBaseModel(
        user_id=userdb.user_id,
        name=userdb.name,
        surname=userdb.surname,
        patronymic=userdb.patronymic,
        email=userdb.email
    )
    return user
