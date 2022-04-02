from datetime import date
from pydantic import BaseModel
from datetime import datetime
from app.models.schemas.base import BaseSchema


class WaterDayAdd(BaseSchema):
    week_day: int
    time_day: str
    water_time: int
    plant_id: int
    active: bool


class WaterDayEdit(BaseSchema):
    id: int
    week_day: int
    time_day: str
    water_time: int
    plant_id: int
    active: bool





class WaterDay(BaseSchema):
    id: int
    week_day: int
    time_day: str
    water_time: int
    plant_id: int
    active: bool
    date_created: datetime
