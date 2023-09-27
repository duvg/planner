from pydantic import BaseModel
from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List

class Event(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  title: str
  image: str
  description: str
  tags: List[str] = Field(sa_column=Column(JSON))
  location: str

  class Config:
    arbitraty_types_allowed = True
    json_schema_extra = {
      "example": {
        "title": "Event Planner API",
        "image": "https://cdn.pixabay.com/photo/2017/04/25/22/28/despaired-2261021_1280.jpg",
        "description": "Example of event planner",
        "tags": ["python", "fastapi", "rest"],
        "location": "Google Meet"
      }
    }

class EventUpdate(SQLModel):
  title: Optional[str]
  image: Optional[str]
  description: Optional[str]
  tags: Optional[List[str]]
  location: Optional[str]

  class Config:
    json_schema_extra = {
      "example": {
        "title": "Event planner to update",
        "image": "https://cdn.pixabay.com/photo/2017/04/25/22/28/despaired-2261021_1280.jpg",
        "description": "Description for event to update",
        "tags": ["python", "fastapi", "swagger"],
        "location": "Google Meet"
      }
    }