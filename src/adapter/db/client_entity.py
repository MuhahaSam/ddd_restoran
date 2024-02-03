from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from db_metadata import meta_data

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
