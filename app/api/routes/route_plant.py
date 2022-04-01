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
    status_code=status.HTTP_200_OK,
    response_model=List[Plant],
    responses={
        200: {
            "model": List[Plant]
        }
    }
)
def list_plant(db: Session = Depends(get_db)):
    return plant.Plant.list_all(session=db)


@router.get(
    '/get/{id}',
    status_code=status.HTTP_200_OK,
    response_model=Plant,
    responses={
        200: {
            "model": Plant
        },
        404: {
            "model": errorMessage
        }
    }
)
def get_plant(id: int, db: Session = Depends(get_db)):
    return plant.Plant.find_by_id(session=db, id=id)


@router.post(
    '/update',
    status_code=status.HTTP_200_OK,
    response_model=Plant,
    responses={
        200: {
            "model": Plant
        },
        404: {
            "model": errorMessage
        }
    }
)
def update_plant(data: PlantEdit, db: Session = Depends(get_db)):
    return plant.Plant.update(session=db, data=data)


@router.put(
    '/create',
    status_code=status.HTTP_201_CREATED,
    response_model=Plant,
    responses={
        201: {
            "model": Plant
        },
        400: {
            "model": errorMessage
        }
    }
)
def create_plant(data: PlantAdd, db: Session = Depends(get_db)):
    return plant.Plant.add(session=db, data=data)


@router.delete(
    '/delete/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {
            "model": None
        },
        404: {
            "model": errorMessage
        }
    }
)
def delete_plant(id:int, response: Response, db: Session = Depends(get_db)):
    temp_res = plant.Plant.delete(session=db, id=id)
    if not isinstance(temp_res, bool):
        response.status_code = status.HTTP_404_NOT_FOUND
        return JSONResponse(status_code=404, content={"message": temp_res})
    return Response(status_code=status.HTTP_204_NO_CONTENT)