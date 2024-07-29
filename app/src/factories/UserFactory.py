from src.models.user import User

class UserFactory:
    @staticmethod
    def create_user(user_id, name, surname, patronymic):
        return User(user_id, name, surname, patronymic)
