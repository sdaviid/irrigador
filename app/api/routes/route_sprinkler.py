from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, Response, status, APIRouter
from fastapi.responses import JSONResponse

from app.models import sprinkler
from app.models.schemas.sprinkler import(
    Sprinkler,
    SprinklerAdd,
    SprinklerEdit
)
from app.models.schemas.base import errorMessage

from app.core.database import get_db


router = APIRouter()


@router.get(
    '/list',
    response_model=List[Sprinkler]
)
def list_sprinkler(db: Session = Depends(get_db)):
    return sprinkler.Sprinkler.list_all(session=db)


@router.get(
    '/get/{id}',
    response_model=Sprinkler
)
def get_sprinkler(id:int, db: Session = Depends(get_db)):
    return sprinkler.Sprinkler.find_by_id(session=db, id=id)


@router.post(
    '/update',
    response_model=Sprinkler
)
def update_sprinkler(data:SprinklerEdit, db: Session = Depends(get_db)):
    return sprinkler.Sprinkler.update(session=db, data=data)


@router.put(
    '/create',
    response_model=Sprinkler
)
def create_sprinkler(data: SprinklerAdd, db: Session = Depends(get_db)):
    return sprinkler.Sprinkler.add(session=db, data=data)


@router.delete(
    '/delete/{id}'
)
def delete_sprinkler(id: int, db: Session = Depends(get_db)):
    return sprinkler.Sprinkler.delete(session=db, id=id)