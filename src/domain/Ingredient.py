from typing import List
from dataclasses import dataclass


@dataclass
class Ingredient:
    id: str
    name: str
    prize_per_kg: float
    expiration_day: int
    menu_gram: float
