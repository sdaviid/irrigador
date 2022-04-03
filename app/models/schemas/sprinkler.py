from datetime import date
from pydantic import Field
from datetime import datetime
from app.models.schemas.plant import Plant
from app.models.schemas.base import BaseSchema


class SprinklerAdd(BaseSchema):
    description: str = Field(title="The description of the item")
    active: bool


class SprinklerEdit(BaseSchema):
    id: int
    description: str
    active: bool


class Sprinkler(BaseSchema):
    id: int
    description: str = Field(title="The description of the item")
    active: bool = Field(True, title="Status of the item")
    date_created: datetime = Field(datetime.now(), title="Date when created the item")
