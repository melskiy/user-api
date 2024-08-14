from src.base.user.models.user_base_model import UserBaseModel
from src.base.user.models.user_db import UserDB


def user_db_adapter(user: UserBaseModel) -> UserDB:
    db_user = UserDB(
        user_id=user.user_id,
        name=user.name,
        surname=user.surname,
        patronymic=user.patronymic,
    )
    return db_user
