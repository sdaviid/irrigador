from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import Date, Boolean, Time, DateTime
from app.core.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship, backref


class Plant(Base):
    __tablename__ = "plant"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(255))
    sprinkler_id = Column(Integer, ForeignKey("sprinkler.id"))
    water_day = relationship("WaterDay", uselist=False, backref=backref("plant"))
    log = relationship("Log", uselist=False, backref=backref("plant"))
    active = Column(Boolean, default=False)
    date_created = Column(Date, default=datetime.utcnow())