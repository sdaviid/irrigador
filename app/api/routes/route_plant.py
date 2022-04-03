from typing import List
from sqlalchemy.orm import Session
from fastapi import(
    Depends,
    Response,
    status,
    APIRouter
)
from fastapi.responses import JSONResponse

from app.models.domain import plant
from app.models.schemas.plant import(
    Plant,
    PlantAdd,
    PlantEdit,
    PlantDetail
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
    response_model=List[PlantDetail],
    responses={
        200: {
            "model": List[PlantDetail]
        }
    }
)
def list_plant(db: Session = Depends(get_db)):
    return plant.Plant.list_all(session=db)


@router.get(
    '/{id}',
    status_code=status.HTTP_200_OK,
    response_model=PlantDetail,
    responses={
        200: {
            "model": PlantDetail
        },
        404: {
            "model": errorMessage
        },
        422: {
            "model": ValidatorError
        }
    }
)
def get_plant(id: int, response: Response, db: Session = Depends(get_db)):
    temp_res = plant.Plant.find_by_id_detail(session=db, id=id)
    if isinstance(temp_res, str):
        response.status_code = status.HTTP_404_NOT_FOUND
        return JSONResponse(status_code=404, content={"message": temp_res})
    return temp_res


@router.post(
    '',
    status_code=status.HTTP_200_OK,
    response_model=Plant,
    responses={
        200: {
            "model": Plant
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
def update_plant(data: PlantEdit, response: Response, db: Session = Depends(get_db)):
    temp_res = plant.Plant.update(session=db, data=data)
    if isinstance(temp_res, dict):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return JSONResponse(status_code=400, content=temp_res)
    elif isinstance(temp_res, str):
        response.status_code = status.HTTP_404_NOT_FOUND
        return JSONResponse(status_code=404, content={"message": temp_res})
    else:
        return temp_res


@router.put(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=Plant,
    responses={
        201: {
            "model": Plant
        },
        400: {
            "model": errorMessageDetail
        },
        422: {
            "model": ValidatorError
        }
    }
)
def create_plant(data: PlantAdd, response: Response, db: Session = Depends(get_db)):
    temp_res = plant.Plant.add(session=db, data=data)
    print(type(temp_res))
    if isinstance(temp_res, dict):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return JSONResponse(status_code=400, content=temp_res)
    return temp_res


@router.delete(
    '/{id}',
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
def delete_plant(id:int, response: Response, db: Session = Depends(get_db)):
    temp_res = plant.Plant.delete(session=db, id=id)
    if not isinstance(temp_res, bool):
        response.status_code = status.HTTP_404_NOT_FOUND
        return JSONResponse(status_code=404, content={"message": temp_res})
    return Response(status_code=status.HTTP_204_NO_CONTENT)