from datetime import date
from pydantic import BaseModel
from datetime import datetime
from app.models.schemas.plant import Plant


class Sprinkler(BaseModel):
    id: int
    description: str
    sensor_id: int
    active: bool
    date_created: datetime
    class Config:
        orm_mode = True