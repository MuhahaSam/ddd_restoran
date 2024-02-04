from typing import List
from dataclasses import dataclass
from datetime import datetime
from Ingredient import Ingredient


@dataclass
class Store:
    id: str
    ingredient: Ingredient
    store_number: int
    inventory: float
