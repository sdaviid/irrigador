from datetime import date
from pydantic import BaseModel
from datetime import datetime


class Log(BaseModel):
    id: int
    plant_id: int
    log_id: int
    date_created: datetime


class LogType(BaseModel):
    id: int
    description: str
    log_type: Log