from dataclasses import dataclass
from enum import Enum


class Role(Enum):
    CHEF = 'chef'
    SU_CHEF = 'su_chef'
    COOK = 'cook'


@dataclass
class User:
    id: str
    role: Role
    name: str
    email: str
    password: str
