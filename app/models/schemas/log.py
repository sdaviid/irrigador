from datetime import date
from pydantic import BaseModel
from datetime import datetime
from app.models.schemas.base import BaseSchema
from typing import Optional

class LogAdd(BaseSchema):
    plant_id: int
    key: str


class Log(BaseSchema):
    id: int
    plant_id: int
    key: str
    date_created: datetime


class LogDetail(BaseSchema):
    id: int
    plant_id: int
    key: str
    plant_description: str
    sprinkler_description: str
    date_created: datetime


class LogHistory(BaseSchema):
    date_start: str
    date_end: Optional[str] = None