from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Table

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
    Column('email', String(length=255), nullable=False, unique=True),
)

client_order_entity = Table(
    "client_order",
    meta_data,
    Column('id', Integer(), primary_key=True),
    Column('client_id', ForeignKey('client.id'), nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('deleted_at', DateTime, nullable=False),
)
