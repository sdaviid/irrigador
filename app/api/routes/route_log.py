from typing import List
from sqlalchemy.orm import Session
from fastapi import(
    Depends,
    Response,
    status,
    APIRouter
)
from fastapi.responses import JSONResponse


from app.models.domain import log
from app.models.schemas.log import(
    Log,
    LogAdd,
    LogDetail,
    LogHistory
)
from app.models.schemas.base import(
    errorMessage,
    ValidatorError,
    errorMessageDetail
)

from app.core.database import get_db


router = APIRouter()


@router.get(
    '/list',
    status_code=status.HTTP_200_OK,
    response_model=List[LogDetail],
    responses={
        200: {
            "model": List[LogDetail]
        }
    }
)
def list_log(db: Session = Depends(get_db)):
    return log.Log.list_all(session=db)



@router.get(
    '/history',
    status_code=status.HTTP_200_OK,
    response_model=List[LogDetail],
    responses={
        200: {
            "model": List[LogDetail]
        },
        400: {
            "model": errorMessageDetail
        }
    }
)
def list_history(date_start: str, response: Response, date_end: str = None, db: Session = Depends(get_db)):
    temp_res = log.Log.find_by_date(session=db, date_start=date_start, date_end=date_end)
    if isinstance(temp_res, dict):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return JSONResponse(status_code=400, content=temp_res)
    return temp_res




@router.get(
    '/get/{id}',
    status_code=status.HTTP_200_OK,
    response_model=LogDetail,
    responses={
        200: {
            "model": LogDetail
        },
        404: {
            "model": errorMessage
        },
        422: {
            "model": ValidatorError
        }
    }
)
def get_log(id: int, response: Response, db: Session = Depends(get_db)):
    temp_res = log.Log.find_by_id(session=db, id=id)
    if isinstance(temp_res, str):
        response.status_code = status.HTTP_404_NOT_FOUND
        return JSONResponse(status_code=404, content={"message": temp_res})
    return temp_res



@router.put(
    '/create',
    status_code=status.HTTP_201_CREATED,
    response_model=Log,
    responses={
        201: {
            "model": Log
        },
        400: {
            "model": errorMessageDetail
        },
        422: {
            "model": ValidatorError
        }
    }
)
def create_log(data: LogAdd, response: Response, db: Session = Depends(get_db)):
    temp_res = log.Log.add(session=db, data=data)
    if not isinstance(temp_res, log.Log):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return JSONResponse(status_code=400, content=temp_res)
    return temp_res
