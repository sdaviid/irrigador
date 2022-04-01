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
    date_created = Column(DateTime, default=datetime.utcnow())
    @classmethod
    def add(cls, session, description, sprinkler_id, active):
        plant = Plant()
        plant.description = description
        plant.sprinkler_id = sprinkler_id
        plant.active = active
        session.add(plant)
        session.commit()
        session.refresh(plant)
        return Plant.find_by_id(session=session, id=plant.id)
    @classmethod
    def list_all(cls, session):
        return session.query(cls).filter().all()
    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).one()