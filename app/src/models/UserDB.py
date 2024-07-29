from sqlalchemy import String, Column
from src.models.base import Base

class UserDB(Base):
    __tablename__ = "users"
    userid = Column(String(100), primary_key=True, index=True)
    lastname = Column(String(100))
    firstname = Column(String(100))
    patronymic = Column(String(100))
    
