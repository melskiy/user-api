from sqlalchemy import String, Column
from sqlalchemy.orm import declarative_base
from sqlalchemy import MetaData


metadata_obj = MetaData(schema="job_title_profile")

Base = declarative_base(metadata=metadata_obj)


class JobTitleDB(Base):
    __tablename__ = "job_title"
    job_title_id = Column(String(100), primary_key=True, index=True)
    job_title_name = Column(String(100))
