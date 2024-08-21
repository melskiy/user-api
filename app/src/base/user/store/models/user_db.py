from sqlalchemy import String, Column

from sqlalchemy.orm import declarative_base
from sqlalchemy import MetaData

metadata_obj = MetaData(schema="userprofile")

Base = declarative_base(metadata=metadata_obj)


class UserDB(Base):
    __tablename__ = "users"
    user_id = Column(String(100), primary_key=True, index=True)
    name = Column(String(100))
    surname = Column(String(100))
    patronymic = Column(String(100))
    email = Column(String(100))
