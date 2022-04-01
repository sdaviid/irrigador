from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, Response, status, APIRouter
from fastapi.responses import JSONResponse

from app.models import sensor
from app.models.schemas.sensor import(
    Sensor,
    SensorAdd,
    SensorEdit
)
from app.models.schemas.base import errorMessage, ValidatorError

from app.core.database import get_db


router = APIRouter()


@router.get(
    '/list',
    status_code=status.HTTP_200_OK,
    response_model=List[Sensor],
    responses={
        200: {
            "model": List[Sensor]
        }
    }
)
def list_sensor(db: Session = Depends(get_db)):
    return sensor.Sensor.list_all(session=db)


@router.get(
    '/get/{id}',
    status_code=status.HTTP_200_OK,
    response_model=Sensor,
    responses={
        200: {
            "model": Sensor
        },
        404: {
            "model": errorMessage
        },
        422: {
            "model": ValidatorError
        }
    }
)
def get_sensor(id: int, response: Response, db: Session = Depends(get_db)):
    response.status_code = status.HTTP_409_CONFLICT
    return sensor.Sensor.find_by_id(session=db, id=id)


@router.post(
    '/update',
    status_code=status.HTTP_200_OK,
    response_model=Sensor,
    responses={
        200: {
            "model": Sensor
        },
        404: {
            "model": errorMessage
        },
        422: {
            "model": ValidatorError
        }
    }

)
def update_sensor(data: SensorEdit, db: Session = Depends(get_db)):
    return sensor.Sensor.update(session=db, data=data)


@router.put(
    '/create',
    status_code=status.HTTP_201_CREATED,
    response_model=Sensor,
    responses={
        201: {
            "model": Sensor
        },
        400: {
            "model": errorMessage
        },
        422: {
            "model": ValidatorError
        }
    }
)
def create_sensor(data:SensorAdd, db: Session = Depends(get_db)):
    return sensor.Sensor.add(session=db, data=data)


@router.delete(
    '/delete/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {
            "model": None
        },
        404: {
            "model": errorMessage
        },
        422: {
            "model": ValidatorError
        }
    }
)
def delete_sensor(id:int, response: Response, db: Session = Depends(get_db)):
    temp_res = sensor.Sensor.delete(session=db, id=id)
    if not isinstance(temp_res, bool):
        response.status_code = status.HTTP_404_NOT_FOUND
        return JSONResponse(status_code=404, content={"message": temp_res})
    return Response(status_code=status.HTTP_204_NO_CONTENT)