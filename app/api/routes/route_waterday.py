from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, Response, status, APIRouter
from fastapi.responses import JSONResponse


from app.models import waterday
from app.models.schemas.waterday import(
    WaterDay,
    WaterDayAdd,
    WaterDayEdit
)
from app.models.schemas.base import errorMessage, ValidatorError

from app.core.database import get_db


router = APIRouter()


@router.get(
    '/list',
    status_code=status.HTTP_200_OK,
    response_model=List[WaterDay],
    responses={
        200: {
            "model": List[WaterDay]
        }
    }
)
def list_water_day(db: Session = Depends(get_db)):
    return waterday.WaterDay.list_all(session=db)


@router.get(
    '/get/{id}',
    status_code=status.HTTP_200_OK,
    response_model=WaterDay,
    responses={
        200: {
            "model": WaterDay
        },
        404: {
            "model": errorMessage
        },
        422: {
            "model": ValidatorError
        }
    }
)
def get_water_day(id: int, db: Session = Depends(get_db)):
    return waterday.WaterDay.find_by_id(session=db, id=id)


@router.post(
    '/update',
    status_code=status.HTTP_200_OK,
    response_model=WaterDay,
    responses={
        200: {
            "model": WaterDay
        },
        404: {
            "model": errorMessage
        },
        422: {
            "model": ValidatorError
        }
    }
)
def update_water_day(data: WaterDayEdit, db: Session = Depends(get_db)):
    return waterday.WaterDay.update(session=db, data=data)


@router.put(
    '/create',
    status_code=status.HTTP_201_CREATED,
    response_model=WaterDay,
    responses={
        201: {
            "model": WaterDay
        },
        400: {
            "model": errorMessage
        },
        422: {
            "model": ValidatorError
        }
    }
)
def create_water_day(data: WaterDayAdd, db: Session = Depends(get_db)):
    return waterday.WaterDay.add(session=db, data=data)


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
def delete_water_day(id:int, response: Response, db: Session = Depends(get_db)):
    temp_res = waterday.WaterDay.delete(session=db, id=id)
    if not isinstance(temp_res, bool):
        response.status_code = status.HTTP_404_NOT_FOUND
        return JSONResponse(status_code=404, content={"message": temp_res})
    return Response(status_code=status.HTTP_204_NO_CONTENT)