class User():
    def __init__(self, user_id, name, surname, patronymic):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def __repr__(self):
        return f"User(id={self.user_id}, name='{self.name}', surname='{self.surname}', patronymic='{self.patronymic}')"
