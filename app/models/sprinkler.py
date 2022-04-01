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
    plant = relationship("Plant", uselist=False, backref=backref("sprinkler"))
    active = Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.utcnow())
    @classmethod
    def add(cls, session, description, sensor_id, active):
        sprinkler = Sprinkler()
        sprinkler.description = description
        sprinkler.sensor_id = sensor_id
        sprinkler.active = active
        session.add(sprinkler)
        session.commit()
        session.refresh(sprinkler)
        return Sprinkler.find_by_id(session=session, id=sprinkler.id)
    @classmethod
    def list_all(cls, session):
        return session.query(cls).filter().all()
    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).one()