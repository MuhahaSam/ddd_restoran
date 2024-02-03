from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Table
# from . import meta_data
from sqlalchemy import MetaData

meta_data = MetaData()

client_order_entity = Table(
    "client_order",
    meta_data,
    Column('id', Integer(), primary_key=True),
    Column('client_id', ForeignKey('client.id'), nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('deleted_at', DateTime, nullable=False),
)
