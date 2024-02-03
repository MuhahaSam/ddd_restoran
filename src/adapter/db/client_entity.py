from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
# from . import meta_data

from sqlalchemy import MetaData

meta_data = MetaData()

client_entity = Table(
    "client",
    meta_data,
    Column('id', Integer(), primary_key=True),
    Column('first_name', String(
        length=255), nullable=False),
    Column('last_name', String(
        length=255), nullable=False),
    Column('password', String(
        length=255), nullable=False),
    email=Column('email', String(length=255), nullable=False, unique=True),
)
