from src.base.user.models.user_base_model import UserBaseModel


def user_adapter(userdb):
    user = UserBaseModel(
        user_id=userdb.user_id,
        name=userdb.name,
        surname=userdb.surname,
        patronymic=userdb.patronymic,
    )
    return user
