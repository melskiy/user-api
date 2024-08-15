from sqlalchemy import String, Column
from src.base.user.models.base import Base


class UserDB(Base):
    __tablename__ = "users"
    user_id = Column(String(100), primary_key=True, index=True)
    name = Column(String(100))
    surname = Column(String(100))
    patronymic = Column(String(100))
    email = Column(String(100))

