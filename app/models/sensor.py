from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import Date, Boolean, Time, DateTime
from app.core.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship, backref


class Sensor(Base):
    __tablename__ = "sensor"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(255))
    sprinkler = relationship("Sprinkler", uselist=False, backref=backref("sensor"))
    active = Column(Boolean, default=False)
    date_created = Column(Date, default=datetime.utcnow())