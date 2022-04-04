from typing import List
from sqlalchemy.orm import Session
from fastapi import(
    Depends,
    Response,
    status,
    APIRouter
)
from fastapi.responses import JSONResponse

from app.models.domain import sprinkler
from app.models.schemas.sprinkler import(
    Sprinkler,
    SprinklerAdd,
    SprinklerEdit
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
    response_model=List[Sprinkler],
    responses={
        200: {
            "model": List[Sprinkler]
        }
    }
)
def list_sprinkler(db: Session = Depends(get_db)):
    """List information about all sprinklers"""
    return sprinkler.Sprinkler.list_all(session=db)


@router.get(
    '/{sprinkler_id}',
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
def get_sprinkler(sprinkler_id:int, response: Response, db: Session = Depends(get_db)):
    """Retrieve information about specific Sprinkler"""
    temp_res = sprinkler.Sprinkler.find_by_id(session=db, id=sprinkler_id)
    if not isinstance(temp_res, sprinkler.Sprinkler):
        response.status_code = status.HTTP_404_NOT_FOUND
        return JSONResponse(status_code=404, content={"message": temp_res})
    return temp_res


@router.post(
    '',
    status_code=status.HTTP_200_OK,
    response_model=Sprinkler,
    responses={
        200: {
            "model": Sprinkler
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
def update_sprinkler(data:SprinklerEdit, response: Response, db: Session = Depends(get_db)):
    """Update specified sprinkler"""
    temp_res = sprinkler.Sprinkler.update(session=db, data=data)
    if not isinstance(temp_res, sprinkler.Sprinkler):
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
    response_model=Sprinkler,
    responses={
        201: {
            "model": Sprinkler
        },
        400: {
            "model": errorMessageDetail
        },
        422: {
            "model": ValidatorError
        }
    }
)
def create_sprinkler(data: SprinklerAdd, response: Response, db: Session = Depends(get_db)):
    """Create a new sprinkler"""
    temp_res = sprinkler.Sprinkler.add(session=db, data=data)
    if not isinstance(temp_res, sprinkler.Sprinkler):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return JSONResponse(status_code=400, content=temp_res)
    return temp_res


@router.delete(
    '/{sprinkler_id}',
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
def delete_sprinkler(sprinkler_id:int, response: Response, db: Session = Depends(get_db)):
    """Delete specified sprinkler"""
    temp_res = sprinkler.Sprinkler.delete(session=db, id=sprinkler_id)
    if not isinstance(temp_res, bool):
        response.status_code = status.HTTP_404_NOT_FOUND
        return JSONResponse(status_code=404, content={"message": temp_res})
    return Response(status_code=status.HTTP_204_NO_CONTENT)