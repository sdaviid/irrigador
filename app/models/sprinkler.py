from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import Date, Boolean, Time, DateTime
from app.core.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship, backref


class Sprinkler(Base):
    __tablename__ = "sprinkler"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(255))
    sensor_id = Column(Integer, ForeignKey("sensor.id"))
    plant = relationship("Plants", uselist=False, backref=backref("sprinkler"))
    log = relationship("Log", uselist=False, backref=backref("sprinkler"))
    active = Column(Boolean, default=False)
    date_created = Column(Date, default=datetime.utcnow())