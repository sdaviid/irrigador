from datetime import date
from pydantic import BaseModel
from datetime import datetime
from app.models.schemas.plant import Plant
from app.models.schemas.base import BaseSchema


class SprinklerAdd(BaseSchema):
    description: str
    sensor_id: int
    active: bool


class Sprinkler(BaseSchema):
    id: int
    description: str
    sensor_id: int
    active: bool
    date_created: datetime
