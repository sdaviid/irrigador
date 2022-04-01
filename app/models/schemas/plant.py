from datetime import date
from pydantic import BaseModel
from datetime import datetime
from app.models.schemas.waterday import WaterDay
from app.models.schemas.log import Log


class Plant(BaseModel):
    id: int
    description: str
    sprinkler_id: int
    active: bool
    date_created: datetime
    class Config:
        orm_mode = True