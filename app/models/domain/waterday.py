from sqlalchemy import(
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.types import(
    Date,
    Boolean,
    Time,
    DateTime
)
from sqlalchemy.orm import(
    relationship,
    backref
)
from app.models.base import ModelBase
from app.core.database import Base
from datetime import datetime

from app.models.domain.plant import Plant
from app.utils.utils import(
    str2time
)


class WaterDay(ModelBase, Base):
    __tablename__ = "waterday"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    week_day = Column(Integer)
    time_day = Column(String(5))
    water_time = Column(Integer)
    plant_id = Column(Integer, ForeignKey("plant.id"))
    active = Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.utcnow())
    @classmethod
    def validate_data(cls, session, data):
        if not Plant.has_id(session=session, id=data.plant_id):
            return {
                "message": "Don't find plant_id specified",
                "exception": f'plant_id {data.plant_id} not found'
            }
        temp_water_time_conversion = str2time(data.time_day)
        if not isinstance(temp_water_time_conversion, datetime):
            return {
                "message": "Time Day must be in format HH:MM - 24 format",
                "exception": temp_water_time_conversion
            }
        if not data.week_day in (0, 6):
            return {
                "message": "Weekday must be between 0-6 (0: Monday/6: Sunday)",
                "exception": f"Weekday {data.week_day} is invalid"
            }
        return True
    @classmethod
    def add(cls, session, data):
        temp_validate = WaterDay.validate_data(session=session, data=data)
        if temp_validate != True:
            return temp_validate
        waterday = WaterDay()
        waterday.week_day = data.week_day
        waterday.time_day = data.time_day
        waterday.water_time = data.water_time
        waterday.plant_id = data.plant_id
        waterday.active = data.active
        session.add(waterday)
        session.commit()
        session.refresh(waterday)
        return WaterDay.find_by_id(session=session, id=waterday.id)
    @classmethod
    def update(cls, session, data):
        if WaterDay.has_id(session=session, id=data.id) == False:
            return "Don't find ID specified"
        temp_validate = WaterDay.validate_data(session=session, data=data)
        if temp_validate != True:
            return temp_validate
        original = WaterDay.find_by_id(session, id=data.id)
        original.week_day = data.week_day
        original.time_day = data.time_day
        original.water_time = data.water_time
        original.plant_id = data.plant_id
        original.active = data.active
        session.commit()
        session.refresh(original)
        return original
    @classmethod
    def list_all(cls, session):
        return session.query(
            cls.id,
            cls.week_day,
            cls.time_day,
            cls.water_time,
            cls.plant_id,
            cls.active,
            Plant.description.label('plant_description'),
            cls.date_created
        ).filter().all()
    @classmethod
    def find_by_id_detail(cls, session, id):
        if cls.has_id(session=session, id=id) == False:
            return "Don't find ID specified"
        return session.query(
            cls.id,
            cls.week_day,
            cls.time_day,
            cls.water_time,
            cls.plant_id,
            cls.active,
            Plant.description.label('plant_description'),
            cls.date_created
        ).filter_by(id=id).first()