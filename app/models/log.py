from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import Date, Boolean, Time, DateTime
from app.core.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship, backref



class Log(Base):
    __tablename__ = "log"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sprinkler_id = Column(Integer, ForeignKey("sprinkler.id"))
    plant_id = Column(Integer, ForeignKey("plant.id"))
    log_id = Column(Integer, ForeignKey("log.id"))
    date_created = Column(DateTime, default=datetime.utcnow())


class LogType(Base):
    __tablename__ = "logtype"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(255))
    log_type = relationship("Log", uselist=False, backref=backref("logtype"))