from app.core.database import Base

class ModelBase(object):
    @classmethod
    def validate_data(cls, session, data):
        pass


    @classmethod
    def add(cls, session, data):
        pass


    @classmethod
    def update(cls, session, data):
        pass


    @classmethod
    def has_id(cls, session, id):
        return True if session.query(cls).filter_by(id=id).count() > 0 else False


    @classmethod
    def delete(cls, session, id):
        if cls.has_id(session=session, id=id) == True:
            session.query(cls).filter_by(id=id).delete()
            session.commit()
            return True
        return "Don't find ID specified"


    @classmethod
    def list_all(cls, session):
        return session.query(cls).filter().all()


    @classmethod
    def find_by_id(cls, session, id):
        if cls.has_id(session=session, id=id) == False:
            return "Don't find ID specified"
        return session.query(cls).filter_by(id=id).first()