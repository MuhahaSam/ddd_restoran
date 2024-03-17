from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import config

Base = declarative_base()
meta_data = MetaData()
engine = create_engine(f'postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}')
session = Session(engine)
