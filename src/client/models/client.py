from dataclasses import dataclass


@dataclass
class Client:
    id: str
    first_name: str
    last_name: str
    password: str
    email: str
