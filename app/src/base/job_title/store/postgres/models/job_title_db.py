from sqlalchemy import String, Column

from src.base.shared.base_sqla_model import Base


class JobTitleDB(Base):
    __tablename__ = "job_title"
    job_title_id = Column(String(100), primary_key=True, index=True)
    job_title_name = Column(String(100))
