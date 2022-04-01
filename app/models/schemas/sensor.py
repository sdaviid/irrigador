from datetime import date
from pydantic import BaseModel
from datetime import datetime
from app.models.schemas.sprinkler import Sprinkler
from app.models.schemas.base import BaseSchema



class SensorAdd(BaseSchema):
    description: str
    active: bool


class SensorEdit(BaseSchema):
    id: int
    description: str
    active: bool


class Sensor(BaseSchema):
    id: int
    description: str
    active: bool
    date_created = datetime


