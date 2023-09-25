from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.event import Event

class User(BaseModel):
  email: EmailStr
  password: str
  events: Optional[List[Event]]

  class Config:
    schema_extra = {
      "example": {
        "email": "user@mail.com",
        "username": "theusername",
        "events": [],
      }
    }

class UserSingIn(BaseModel):
  email: EmailStr
  password: str

  class Config:
    json_schema_extra = {
      "example": {
        "email": "user@mail.com",
        "password": "datapass",
        "events": [],
      }
    }