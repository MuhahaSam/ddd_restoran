from datetime import date
from typing import List
from .menu import Menu
from dataclasses import dataclass


@dataclass
class Order:
    id: str
    create_at: date
    menu_list: Menu
