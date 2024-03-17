from pydantic import BaseModel, Field, EmailStr


class CreateClientDto(BaseModel):
    email: EmailStr = Field(min_length=1)
    password: str = Field(min_length=6)
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
