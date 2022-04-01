from datetime import date
from pydantic import BaseModel
from datetime import datetime
from app.models.schemas.base import BaseSchema

class LogAdd(BaseSchema):
    plant_id: int
    log_id: int


class Log(BaseSchema):
    id: int
    plant_id: int
    log_id: int
    date_created: datetime


class LogType(BaseSchema):
    id: int
    description: str
    log_type: Log