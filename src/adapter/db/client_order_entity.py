from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Table
from db_metadata import meta_data


client_order_entity = Table(
    "client_order",
    meta_data,
    Column('id', Integer(), primary_key=True),
    Column('client_id', ForeignKey('client.id'), nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('deleted_at', DateTime, nullable=False),
)
