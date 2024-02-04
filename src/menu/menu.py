from Ingredient.Ingredient import Ingredient
from typing import List
from dataclasses import dataclass


@dataclass
class Menu:
    id: str
    name: str
    prize: int
    weight: float
    kall: int
    ingredient_list: List[Ingredient]
