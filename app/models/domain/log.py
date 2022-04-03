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

from app.utils.utils import(
    str2date
)


class Log(ModelBase, Base):
    __tablename__ = "log"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    plant_id = Column(Integer, ForeignKey("plant.id"))
    key = Column(String(15))
    date_created = Column(DateTime, default=datetime.utcnow())
    @classmethod
    def validate_data(cls, session, data):
        if not Plant.has_id(session=session, id=data.plant_id):
            return {
                "message": "Don't find plant_id specified",
                "exception": f'plant_id {data.plant_id} not found'
            }
        if not data.key.lower() in ('ok', 'fail'):
            return {
                "message": "Key must be OK or FAIL",
                "exception": "Unrecognized key data"
            }
        return True
    @classmethod
    def add(cls, session, data):
        temp_validate = cls.validate_data(session=session, data=data)
        if temp_validate != True:
            return temp_validate
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
    @classmethod
    def find_by_id(cls, session, id):
        if cls.has_id(session=session, id=id) == False:
            return "Don't find ID specified"
        return session.query(
            cls.id,
            cls.plant_id,
            cls.key,
            Plant.description.label('plant_description'),
            Sprinkler.description.label('sprinkler_description'),
            cls.date_created
        ).filter_by(id=id).first()
    @classmethod
    def find_by_date(cls, session, date_start, date_end=None):
        date_start = str2date(date_start)
        date_end = date_end if date_end == None else str2date(date_end)
        if not isinstance(date_start, datetime):
            return {
                "message": "date_start must be in format YYYY-MM-DD",
                "exception": date_start
            }
        elif date_end != None and isinstance(date_end, datetime) != True:
            return {
                "message": "date_end must be in format YYYY-MM-DD",
                "exception": date_end
            }
        else:
            if date_end != None:
                date_end = date_end.replace(hour=23).replace(minute=59).replace(second=59)
                return session.query(
                    cls.id,
                    cls.plant_id,
                    cls.key,
                    Plant.description.label('plant_description'),
                    Sprinkler.description.label('sprinkler_description'),
                    cls.date_created
                ).filter(
                    cls.date_created >= date_start
                ).filter(
                    cls.date_created <= date_end
                ).all()
            else:
                return session.query(
                    cls.id,
                    cls.plant_id,
                    cls.key,
                    Plant.description.label('plant_description'),
                    Sprinkler.description.label('sprinkler_description'),
                    cls.date_created
                ).filter(
                    cls.date_created >= date_start
                ).all()




