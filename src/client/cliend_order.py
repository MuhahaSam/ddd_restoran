from typing import List
from dataclasses import dataclass
from datetime import datetime
from menu import Menu
from src.client.client import Client


@dataclass
class ClientOrder:
    id: str
    create_at: datetime
    client: Client
    menus: List[Menu]
