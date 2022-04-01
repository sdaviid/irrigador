from datetime import date
from pydantic import BaseModel
from datetime import datetime


class WaterDay(BaseModel):
    id: int
    week_day: int
    water_time: datetime
    plant_id: int
    active: bool
    date_created: datetime
    class Config:
        orm_mode = True