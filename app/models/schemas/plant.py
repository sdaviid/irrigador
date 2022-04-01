from datetime import date
from pydantic import BaseModel
from datetime import datetime
from app.models.schemas.waterday import WaterDay
from app.models.schemas.log import Log
from app.models.schemas.base import BaseSchema


class PlantAdd(BaseSchema):
    description: str
    sprinkler_id: int
    active: bool


class Plant(BaseSchema):
    id: int
    description: str
    sprinkler_id: int
    active: bool
    date_created: datetime
