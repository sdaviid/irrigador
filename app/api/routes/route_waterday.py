from typing import List
from sqlalchemy.orm import Session
from fastapi import(
    Depends,
    Response,
    status,
    APIRouter
)
from fastapi.responses import JSONResponse
from datetime import datetime

from app.models.domain import waterday
from app.models.schemas.waterday import(
    WaterDay,
    WaterDayAdd,
    WaterDayEdit,
    WaterDayDetail
)
from app.models.schemas.base import(
    errorMessage,
    ValidatorError,
    errorMessageDetail
)

from app.core.database import get_db



router = APIRouter()


@router.get(
    '',
    status_code=status.HTTP_200_OK,
    response_model=List[WaterDayDetail],
    responses={
        200: {
            "model": List[WaterDayDetail]
        }
    }
)
def list_water_day(db: Session = Depends(get_db)):
    return waterday.WaterDay.list_all(session=db)


@router.get(
    '/{waterDayId}',
    status_code=status.HTTP_200_OK,
    response_model=WaterDayDetail,
    responses={
        200: {
            "model": WaterDayDetail
        },
        404: {
            "model": errorMessage
        },
        422: {
            "model": ValidatorError
        }
    }
)
def get_water_day(waterDayId: int, response: Response, db: Session = Depends(get_db)):
    temp_res = waterday.WaterDay.find_by_id_detail(session=db, id=waterDayId)
    if isinstance(temp_res, str):
        response.status_code = status.HTTP_404_NOT_FOUND
        return JSONResponse(status_code=404, content={"message": temp_res})
    return temp_res


@router.post(
    '',
    status_code=status.HTTP_200_OK,
    response_model=WaterDay,
    responses={
        200: {
            "model": WaterDay
        },
        400: {
            "model": errorMessageDetail
        },
        404: {
            "model": errorMessage
        },
        422: {
            "model": ValidatorError
        }
    }
)
def update_water_day(data: WaterDayEdit, response: Response, db: Session = Depends(get_db)):
    temp_res = waterday.WaterDay.update(session=db, data=data)
    if not isinstance(temp_res, waterday.WaterDay):
        if isinstance(temp_res, dict):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return JSONResponse(status_code=400, content=temp_res)
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return JSONResponse(status_code=404, content={"message": temp_res})
    return temp_res


@router.put(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=WaterDay,
    responses={
        201: {
            "model": WaterDay
        },
        400: {
            "model": errorMessageDetail
        },
        422: {
            "model": ValidatorError
        }
    }
)
def create_water_day(data: WaterDayAdd, response: Response, db: Session = Depends(get_db)):
    temp_res = waterday.WaterDay.add(session=db, data=data)
    if isinstance(temp_res, dict):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return JSONResponse(status_code=400, content=temp_res)
    return temp_res


@router.delete(
    '/{waterDayId}',
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
def delete_water_day(waterDayId:int, response: Response, db: Session = Depends(get_db)):
    temp_res = waterday.WaterDay.delete(session=db, id=waterDayId)
    if not isinstance(temp_res, bool):
        response.status_code = status.HTTP_404_NOT_FOUND
        return JSONResponse(status_code=404, content={"message": temp_res})
    return Response(status_code=status.HTTP_204_NO_CONTENT)