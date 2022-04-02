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



class Log(ModelBase, Base):
    __tablename__ = "log"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    plant_id = Column(Integer, ForeignKey("plant.id"))
    date_created = Column(DateTime, default=datetime.utcnow())
    @classmethod
    def add(cls, session, data):
        log = Log()
        log.plant_id = data.plant_id
        log.log_id = data.log_id
        session.add(log)
        session.commit()
        session.refresh(log)
        return Log.find_by_id(session=session, id=log.id)



