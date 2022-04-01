from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import Date, Boolean, Time, DateTime
from app.core.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship, backref


class WaterDay(Base):
    __tablename__ = "waterday"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    week_day = Column(Integer)
    water_time = Column(Time)
    plant_id = Column(Integer, ForeignKey("plant.id"))
    active = Column(Boolean, default=False)
    date_created = Column(Date, default=datetime.utcnow())