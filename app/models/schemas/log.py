from datetime import date
from pydantic import Field
from datetime import datetime
from app.models.schemas.base import BaseSchema
from typing import Optional

class LogAdd(BaseSchema):
    plant_id: int = Field(title="Relation plant (ID)")
    key: str = Field(title="Key log type", description="OK or FAIL")


class Log(BaseSchema):
    id: int
    plant_id: int = Field(title="Relation plant (ID)")
    key: str = Field(title="Key log type", description="OK or FAIL")
    date_created: datetime = Field(datetime.now(), title="Date when created the log")


class LogDetail(BaseSchema):
    id: int
    plant_id: int = Field(title="Relation plant (ID)")
    key: str = Field(title="Key log type", description="OK or FAIL")
    plant_description: str = Field(title="Relation plant (Description)")
    sprinkler_description: str = Field(title="Relation sprinkler (Description)")
    date_created: datetime = Field(datetime.now(), title="Date when created the log")
