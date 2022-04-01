from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import Date, Boolean, Time, DateTime
from app.core.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship, backref


class WaterDay(Base):
    __tablename__ = "waterday"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    week_day = Column(Integer)
    water_time = Column(Integer)
    plant_id = Column(Integer, ForeignKey("plant.id"))
    active = Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.utcnow())
    @classmethod
    def add(cls, session, week_day, water_time, plant_id, active):
        waterday = WaterDay()
        waterday.week_day = week_day
        waterday.water_time = water_time
        waterday.plant_id = plant_id
        waterday.active = active
        session.add(waterday)
        session.commit()
        session.refresh(waterday)
        return WaterDay.find_by_id(session=session, id=waterday.id)
    @classmethod
    def list_all(cls, session):
        return session.query(cls).filter().all()
    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).one()