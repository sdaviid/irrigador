from app.api.routes import route_sensor
from app.api.routes import route_sprinkler
from app.api.routes import route_plant
from app.api.routes import route_waterday
from app.api.routes import route_log
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_sensor.router, prefix="/sensor", tags=["sensor"])
api_router.include_router(route_sprinkler.router, prefix="/sprinkler", tags=["sprinkler"])
api_router.include_router(route_plant.router, prefix="/plant", tags=["plant"])
api_router.include_router(route_waterday.router, prefix="/waterday", tags=["waterday"])
api_router.include_router(route_log.router, prefix="/log", tags=["log"])