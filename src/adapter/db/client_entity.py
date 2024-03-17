from sqlalchemy import Column, Integer, String
from . import Base


class ClientEntity(Base):

    __tablename__ = "client"

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(length=255), nullable=False)
    last_name = Column(String(length=255), nullable=False)
    password = Column(String(length=255), nullable=False)
    email = Column(String(length=255), nullable=False)
