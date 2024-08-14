from src.base.user.models.user_db import UserDB


def user_db_adapter(user):
    db_user = UserDB(
        user_id=user.user_id,
        name=user.name,
        surname=user.surname,
        patronymic=user.patronymic,
    )
    return db_user
