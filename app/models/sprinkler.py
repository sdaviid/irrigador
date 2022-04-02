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
from app.core.database import Base
from datetime import datetime


class Sprinkler(Base):
    __tablename__ = "sprinkler"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(255))
    plant = relationship("Plant", uselist=False, backref=backref("sprinkler"))
    active = Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.utcnow())
    @classmethod
    def add(cls, session, data):
        sprinkler = Sprinkler()
        sprinkler.description = data.description
        sprinkler.sensor_id = data.sensor_id
        sprinkler.active = data.active
        session.add(sprinkler)
        session.commit()
        session.refresh(sprinkler)
        return Sprinkler.find_by_id(session=session, id=sprinkler.id)
    @classmethod
    def update(cls, session, data):
        if Sprinkler.has_id(session=session, id=data.id) == False:
            return "Don't find ID specified"
        original = Sprinkler.find_by_id(session, id=data.id)
        original.description = data.description
        original.sensor_id = data.sensor_id
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
        if Sprinkler.has_id(session=session, id=id) == False:
            return "Don't find ID specified"
        return session.query(cls).filter_by(id=id).one()