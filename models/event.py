from pydantic import BaseModel
from typing import List

class Event(BaseModel):
  id: int
  title: str
  image: str
  description: str
  tags: List[str]
  location: str

  class Config:
    json_schema_extra = {
      "example": {
        "title": "Event Planner API",
        "image": "https://cdn.pixabay.com/photo/2017/04/25/22/28/despaired-2261021_1280.jpg",
        "description": "Example of event planner",
        "tags": ["python", "fastapi", "rest"],
        "location": "Google Meet"
      }
    }
