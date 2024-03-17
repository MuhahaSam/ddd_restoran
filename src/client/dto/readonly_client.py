from pydantic import BaseModel, Field, EmailStr
from dataclasses import dataclass

@dataclass
class ReadOnlyClient:
    id: str
    first_name: str
    last_name: str
    email: str