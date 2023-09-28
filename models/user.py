from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.event import Event

class User(Document):
  email: EmailStr
  password: str
  events: Optional[List[Link[Event]]]

  class Settings:
    name = "users"

  class Config:
    json_schema_extra = {
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