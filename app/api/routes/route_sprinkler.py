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
from app.models.schemas.base import errorMessage, ValidatorError

from app.core.database import get_db


router = APIRouter()


@router.get(
    '/list',
    status_code=status.HTTP_200_OK,
    response_model=List[Sprinkler],
    responses={
        200: {
            "model": List[Sprinkler]
        }
    }
)
def list_sprinkler(db: Session = Depends(get_db)):
    return sprinkler.Sprinkler.list_all(session=db)


@router.get(
    '/get/{id}',
    status_code=status.HTTP_200_OK,
    response_model=Sprinkler,
    responses={
        200: {
            "model": Sprinkler
        },
        404: {
            "model": errorMessage
        },
        422: {
            "model": ValidatorError
        }
    }
)
def get_sprinkler(id:int, db: Session = Depends(get_db)):
    return sprinkler.Sprinkler.find_by_id(session=db, id=id)


@router.post(
    '/update',
    status_code=status.HTTP_200_OK,
    response_model=Sprinkler,
    responses={
        200: {
            "model": Sprinkler
        },
        404: {
            "model": errorMessage
        },
        422: {
            "model": ValidatorError
        }
    }
)
def update_sprinkler(data:SprinklerEdit, response: Response, db: Session = Depends(get_db)):
    temp_res = sprinkler.Sprinkler.update(session=db, data=data)
    if not isinstance(temp_res, sprinkler.Sprinkler):
        response.status_code = status.HTTP_404_NOT_FOUND
        return JSONResponse(status_code=404, content={"message": temp_res})
    return temp_res



@router.put(
    '/create',
    status_code=status.HTTP_201_CREATED,
    response_model=Sprinkler,
    responses={
        201: {
            "model": Sprinkler
        },
        400: {
            "model": errorMessage
        },
        422: {
            "model": ValidatorError
        }
    }
)
def create_sprinkler(data: SprinklerAdd, db: Session = Depends(get_db)):
    return sprinkler.Sprinkler.add(session=db, data=data)


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
def delete_sprinkler(id:int, response: Response, db: Session = Depends(get_db)):
    temp_res = sprinkler.Sprinkler.delete(session=db, id=id)
    if not isinstance(temp_res, bool):
        response.status_code = status.HTTP_404_NOT_FOUND
        return JSONResponse(status_code=404, content={"message": temp_res})
    return Response(status_code=status.HTTP_204_NO_CONTENT)