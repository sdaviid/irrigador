from datetime import date
from pydantic import Field
from datetime import datetime
from app.models.schemas.waterday import WaterDay
from app.models.schemas.log import Log
from app.models.schemas.base import BaseSchema


class PlantAdd(BaseSchema):
    description: str = Field(title="The description of the plant")
    sprinkler_id: int = Field(title="Relation sprinkler (ID)")
    active: bool = Field(True, title="Status of the sprinkler")


class PlantEdit(BaseSchema):
    id: int
    description: str = Field(title="The description of the plant")
    sprinkler_id: int = Field(title="Relation sprinkler (ID)")
    active: bool = Field(True, title="Status of the sprinkler")



class Plant(BaseSchema):
    id: int
    description: str = Field(title="The description of the plant")
    sprinkler_id: int = Field(title="Relation sprinkler (ID)")
    active: bool = Field(True, title="Status of the sprinkler")
    date_created: datetime = Field(datetime.now(), title="Date when created the plant")


class PlantDetail(BaseSchema):
    id: int
    description: str = Field(title="The description of the plant")
    sprinkler_id: int = Field(title="Relation sprinkler (ID)")
    active: bool = Field(True, title="Status of the sprinkler")
    sprinkler_description: str
    date_created: datetime = Field(datetime.now(), title="Date when created the plant")