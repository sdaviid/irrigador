from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, Response, status, APIRouter
from fastapi.responses import JSONResponse

from app.models import plant
from app.models.schemas.plant import(
    Plant,
    PlantAdd,
    PlantEdit
)
from app.models.schemas.base import errorMessage

from app.core.database import get_db

router = APIRouter()


@router.get(
    '/list',
    response_model=List[Plant]
)
def list_plant(db: Session = Depends(get_db)):
    return plant.Plant.list_all(session=db)


@router.get(
    '/get/{id}',
    response_model=Plant
)
def get_plant(id: int, db: Session = Depends(get_db)):
    return plant.Plant.find_by_id(session=db, id=id)


@router.post(
    '/update',
    response_model=Plant
)
def update_plant(data: PlantEdit, db: Session = Depends(get_db)):
    return plant.Plant.update(session=db, data=data)


@router.put(
    '/create',
    response_model=Plant
)
def create_plant(data: PlantAdd, db: Session = Depends(get_db)):
    return plant.Plant.add(session=db, data=data)


@router.delete(
    '/delete/{id}'
)
def delete_plant(id: int, db: Session = Depends(get_db)):
    return plant.Plant.delete(session=db, id=id)