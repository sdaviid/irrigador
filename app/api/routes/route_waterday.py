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
from app.models.schemas.base import errorMessage

from app.core.database import get_db


router = APIRouter()


@router.get(
    '/list',
    response_model=List[WaterDay]
)
def list_water_day(db: Session = Depends(get_db)):
    return waterday.WaterDay.list_all(session=db)


@router.get(
    '/get/{id}',
    response_model=WaterDay
)
def get_water_day(id: int, db: Session = Depends(get_db)):
    return waterday.WaterDay.find_by_id(session=db, id=id)


@router.post(
    '/update',
    response_model=WaterDay
)
def update_water_day(data: WaterDayEdit, db: Session = Depends(get_db)):
    return waterday.WaterDay.update(session=db, data=data)


@router.put(
    '/create',
    response_model=WaterDay
)
def create_water_day(data: WaterDayAdd, db: Session = Depends(get_db)):
    return waterday.WaterDay.add(session=db, data=data)


@router.delete(
    '/delete/{id}'
)
def delete_water_day(id: int, db: Session = Depends(get_db)):
    return waterday.WaterDay.delete(session=db, id=id)