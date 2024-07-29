from sqlalchemy.orm import declarative_base
from sqlalchemy import MetaData


metadata_obj = MetaData(schema='UserProfile')

Base = declarative_base(metadata=metadata_obj)
