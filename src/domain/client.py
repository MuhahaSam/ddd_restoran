from dataclasses import dataclass


@dataclass
class Client:
    id: str
    email: str
    password: str
    first_name: str
    last_name: str
