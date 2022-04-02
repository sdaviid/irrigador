from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, Response, status, APIRouter
from fastapi.responses import JSONResponse


from app.models.domain import log
from app.models.schemas.log import(
    Log,
    LogType,
    LogAdd
)
from app.models.schemas.base import errorMessage, ValidatorError

from app.core.database import get_db


router = APIRouter()


@router.get(
    '/list',
    status_code=status.HTTP_200_OK,
    response_model=List[Log],
    responses={
        200: {
            "model": List[Log]
        }
    }
)
def list_log(db: Session = Depends(get_db)):
    return log.Log.list_all(session=db)


@router.get(
    '/get/{id}',
    status_code=status.HTTP_200_OK,
    response_model=Log,
    responses={
        200: {
            "model": Log
        },
        404: {
            "model": errorMessage
        },
        422: {
            "model": ValidatorError
        }
    }
)
def get_log(id: int, db: Session = Depends(get_db)):
    return log.Log.find_by_id(session=db, id=id)



@router.put(
    '/create',
    status_code=status.HTTP_201_CREATED,
    response_model=Log,
    responses={
        201: {
            "model": Log
        },
        400: {
            "model": errorMessage
        },
        422: {
            "model": ValidatorError
        }
    }
)
def create_log(data: LogAdd, db: Session = Depends(get_db)):
    return log.Log.add(session=db, data=data)
