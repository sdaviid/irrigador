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


class Sprinkler(ModelBase, Base):
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
        original.active = data.active
        session.commit()
        session.refresh(original)
        return original