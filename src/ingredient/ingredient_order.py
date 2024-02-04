from typing import List
from dataclasses import dataclass
from datetime import datetime


@dataclass
class IngredientOrder:
    id: str
    delivery_company: str
    order_date: datetime
    order_weight: float
