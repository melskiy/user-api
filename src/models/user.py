from sqlalchemy import Column, String
from src.models.base import Base


class User(Base):
    __tablename__ = 'User'
    client_id = Column(String(7), primary_key=True)
    name = Column(String(32))
    surname = Column(String(32))
    patronymic = Column(String(32))