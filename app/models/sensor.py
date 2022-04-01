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
    date_created = Column(DateTime, default=datetime.utcnow())
    @classmethod
    def add(cls, session, data):
        sensor = Sensor()
        sensor.description = data.description
        sensor.active = data.active
        session.add(sensor)
        session.commit()
        session.refresh(sensor)
        return Sensor.find_by_id(session=session, id=sensor.id)
    @classmethod
    def update(cls, session, data):
        original = Sensor.find_by_id(session, id=data.id)
        original.description = data.description
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
        return session.query(cls).filter_by(id=id).one()