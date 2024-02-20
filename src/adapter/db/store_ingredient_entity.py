from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Table
# from . import meta_data
from sqlalchemy import MetaData

meta_data = MetaData()

client_order_entity = Table(
    "store_ingredient",
    meta_data,
    Column('id', Integer(), primary_key=True),
    Column('name', String(), nullable=False),
    Column('prize', Integer(), nullable=False),
    Column('where_from', String(), nullable=False),
    Column('order_date', DateTime(), nullable=False),
    Column('expiration_day', Integer(), nullable=False), #how many day left
    Column('inventory(kg)', Integer(), nullable=False),
)
