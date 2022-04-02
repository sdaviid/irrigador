from datetime import date
from pydantic import BaseModel
from datetime import datetime
from app.models.schemas.base import BaseSchema

class LogAdd(BaseSchema):
    plant_id: int
    key: str


class Log(BaseSchema):
    id: int
    plant_id: int
    key: str
    date_created: datetime


