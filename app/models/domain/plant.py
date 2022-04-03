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
from app.models.base import ModelBase
from app.core.database import Base
from datetime import datetime

from app.models.domain.sprinkler import Sprinkler


class Plant(ModelBase, Base):
    __tablename__ = "plant"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(255))
    sprinkler_id = Column(Integer, ForeignKey("sprinkler.id"))
    water_day = relationship("WaterDay", uselist=False, backref=backref("plant"))
    log = relationship("Log", uselist=False, backref=backref("plant"))
    active = Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.utcnow())
    @classmethod
    def validate_data(cls, session, data):
        if not Sprinkler.has_id(session=session, id=data.sprinkler_id):
            return {
                "message": "Don't find sprinkler_id specified",
                "exception": f'sprinkler_id {data.sprinkler_id} not found'
            }
        return True
    @classmethod
    def add(cls, session, data):
        temp_validate = Plant.validate_data(session=session, data=data)
        if temp_validate != True:
            return temp_validate
        plant = Plant()
        plant.description = data.description
        plant.sprinkler_id = data.sprinkler_id
        plant.active = data.active
        session.add(plant)
        session.commit()
        session.refresh(plant)
        return Plant.find_by_id(session=session, id=plant.id)
    @classmethod
    def update(cls, session, data):
        if Plant.has_id(session=session, id=data.id) == False:
            return "Don't find ID specified"
        temp_validate = Plant.validate_data(session=session, data=data)
        if temp_validate != True:
            return temp_validate
        original = Plant.find_by_id(session, id=data.id)
        original.description = data.description
        original.sprinkler_id = data.sprinkler_id
        original.active = data.active
        session.commit()
        session.refresh(original)
        return original
    @classmethod
    def list_all(cls, session):
        return session.query(
            cls.id,
            cls.description,
            cls.sprinkler_id,
            cls.active,
            Sprinkler.description.label('sprinkler_description'),
            cls.date_created
        ).filter().all()
    @classmethod
    def find_by_id_detail(cls, session, id):
        if cls.has_id(session=session, id=id) == False:
            return "Don't find ID specified"
        return session.query(
            cls.id,
            cls.description,
            cls.sprinkler_id,
            cls.active,
            Sprinkler.description.label('sprinkler_description'),
            cls.date_created
        ).filter_by(id=id).first()