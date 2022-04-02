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

from app.models.domain.plant import Plant
from app.models.domain.sprinkler import Sprinkler


class Log(ModelBase, Base):
    __tablename__ = "log"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    plant_id = Column(Integer, ForeignKey("plant.id"))
    key = Column(String(15))
    date_created = Column(DateTime, default=datetime.utcnow())
    @classmethod
    def add(cls, session, data):
        log = Log()
        log.plant_id = data.plant_id
        log.key = data.key
        session.add(log)
        session.commit()
        session.refresh(log)
        return Log.find_by_id(session=session, id=log.id)
    @classmethod
    def list_all(cls, session):
        return session.query(
            cls.id,
            cls.plant_id,
            cls.key,
            Plant.description.label('plant_description'),
            Sprinkler.description.label('sprinkler_description'),
            cls.date_created
        ).filter().all()



