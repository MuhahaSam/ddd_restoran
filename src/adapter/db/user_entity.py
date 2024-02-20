from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Table, Enum
# from . import meta_data
from sqlalchemy import MetaData

meta_data = MetaData()

role_entity = Table(
    "role",
    meta_data,
)

user_entity = Table(
    "user",
    meta_data,
    Column('id', Integer(), primary_key=True),
    Column('name', String(), nullable=False),
    Column('email', String(length=255), nullable=False, unique=True),
    Column('password', DateTime, nullable=False),
    Column('role', Enum('chef', 'su_chef', 'cook'), nullable= False),
)
