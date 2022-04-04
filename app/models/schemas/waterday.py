from datetime import date
from pydantic import Field
from datetime import datetime
from app.models.schemas.base import BaseSchema


class WaterDayAdd(BaseSchema):
    week_day: int = Field(title="Day of week to water", description="Day of week between 0-6 (0: Monday/6: Sunday)")
    time_day: str = Field(title="Hour of day to water", description="Hour in 24 format HH:MM")
    water_time: int = Field(title="Water for X seconds")
    plant_id: int = Field(title="Relation plant (ID)")
    active: bool = Field(title="Status of the timer")


class WaterDayEdit(BaseSchema):
    id: int
    week_day: int = Field(title="Day of week to water", description="Day of week between 0-6 (0: Monday/6: Sunday)")
    time_day: str = Field(title="Hour of day to water", description="Hour in 24 format HH:MM")
    water_time: int = Field(title="Water for X seconds")
    plant_id: int = Field(title="Relation plant (ID)")
    active: bool = Field(title="Status of the timer")


class WaterDay(BaseSchema):
    id: int
    week_day: int = Field(title="Day of week to water", description="Day of week between 0-6 (0: Monday/6: Sunday)")
    time_day: str = Field(title="Hour of day to water", description="Hour in 24 format HH:MM")
    water_time: int = Field(title="Water for X seconds")
    plant_id: int = Field(title="Relation plant (ID)")
    active: bool = Field(title="Status of the timer")
    date_created: datetime


class WaterDayDetail(BaseSchema):
    id: int
    week_day: int = Field(title="Day of week to water", description="Day of week between 0-6 (0: Monday/6: Sunday)")
    time_day: str = Field(title="Hour of day to water", description="Hour in 24 format HH:MM")
    water_time: int = Field(title="Water for X seconds")
    plant_id: int = Field(title="Relation plant (ID)")
    active: bool = Field(title="Status of the timer")
    plant_description: str = Field(title="Relation plant (Description)")
    date_created: datetime = Field(datetime.now(), title="Date when created the timer")
