from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, Response, status, APIRouter
from fastapi.responses import JSONResponse


from app.models import log
from app.models.schemas.log import(
    Log,
    LogType,
    LogAdd
)
from app.models.schemas.base import errorMessage

from app.core.database import get_db


router = APIRouter()


@router.get(
    '/list',
    response_model=List[Log]
)
def list_log(db: Session = Depends(get_db)):
    return log.Log.list_all(session=db)


@router.get(
    '/get/{id}',
    response_model=Log
)
def get_log(id: int, db: Session = Depends(get_db)):
    return log.Log.find_by_id(session=db, id=id)



@router.put(
    '/create',
    response_model=Log
)
def create_log(data: LogAdd, db: Session = Depends(get_db)):
    return log.Log.add(session=db, data=data)
