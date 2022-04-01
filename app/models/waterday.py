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
    def add(cls, session, data):
        waterday = WaterDay()
        waterday.week_day = data.week_day
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
        original = WaterDay.find_by_id(session, id=data.id)
        original.week_day = data.week_day
        original.water_time = data.water_time
        original.plant_id = data.plant_id
        original.active = data.active
        session.commit()
        session.refresh(original)
        return original
    @classmethod
    def has_id(cls, session, id):
        return True if session.query(cls).filter_by(id=id).count() > 0 else False
    @classmethod
    def delete(cls, session, id):
        if Sensor.has_id(session=session, id=id) == True:
            session.query(cls).filter_by(id=id).delete()
            session.commit()
            return True
        return "Don't find ID specified"
    @classmethod
    def list_all(cls, session):
        return session.query(cls).filter().all()
    @classmethod
    def find_by_id(cls, session, id):
        if WaterDay.has_id(session=session, id=id) == False:
            return "Don't find ID specified"
        return session.query(cls).filter_by(id=id).one()