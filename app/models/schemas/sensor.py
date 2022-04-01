from datetime import date
from pydantic import BaseModel
from datetime import datetime
from app.models.schemas.sprinkler import Sprinkler


class Sensor(BaseModel):
    id: int
    description: str
    active: bool
    date_created: datetime
    class Config:
        orm_mode = True