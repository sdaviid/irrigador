from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

#importing models
#from app.models.sensor import Sensor
from app.models import sensor
from app.models import sprinkler
from app.models import plant
from app.models import waterday
from app.models import log



#importing schemas
from app.models.schemas.sensor import(
    Sensor,
    SensorAdd,
    SensorEdit
)
from app.models.schemas.sprinkler import(
    Sprinkler,
    SprinklerAdd,
    SprinklerEdit
)
from app.models.schemas.plant import(
    Plant,
    PlantAdd,
    PlantEdit
)
from app.models.schemas.waterday import(
    WaterDay,
    WaterDayAdd,
    WaterDayEdit
)
from app.models.schemas.log import(
    Log,
    LogType,
    LogAdd
)
from app.core.database import SessionLocal, engine, Base

from datetime import datetime

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



#ROUTES

############## SENSORS

@app.get('/sensor/list', response_model=List[Sensor], tags=["sensor"])
def list_sensor(db: Session = Depends(get_db)):
    return sensor.Sensor.list_all(session=db)


@app.get('/sensor/get/{id}', response_model=Sensor, tags=["sensor"])
def get_sensor(id: int, db: Session = Depends(get_db)):
    return sensor.Sensor.find_by_id(session=db, id=id)


@app.post('/sensor/update', tags=["sensor"])
def update_sensor(data: SensorEdit, db: Session = Depends(get_db)):
    return sensor.Sensor.update(session=db, data=data)


@app.put('/sensor/create', response_model=Sensor, tags=["sensor"])
def create_sensor(data:SensorAdd, db: Session = Depends(get_db)):
    return sensor.Sensor.add(session=db, data=data)


@app.delete('/sensor/delete/{id}', tags=["sensor"])
def delete_sensor(id:int, db: Session = Depends(get_db)):
    return sensor.Sensor.delete(session=db, id=id)


############## SENSORS END

############## SPRINKLER

@app.get('/sprinkler/list', response_model=List[Sprinkler], tags=["sprinkler"])
def list_sprinkler(db: Session = Depends(get_db)):
    return sprinkler.Sprinkler.list_all(session=db)


@app.get('/sprinkler/get/{id}', response_model=Sprinkler, tags=["sprinkler"])
def get_sprinkler(id:int, db: Session = Depends(get_db)):
    return sprinkler.Sprinkler.find_by_id(session=db, id=id)


@app.post('/sprinkler/update', response_model=Sprinkler, tags=["sprinkler"])
def update_sprinkler(data:SprinklerEdit, db: Session = Depends(get_db)):
    return sprinkler.Sprinkler.update(session=db, data=data)


@app.put('/sprinkler/create', response_model=Sprinkler, tags=["sprinkler"])
def create_sprinkler(data: SprinklerAdd, db: Session = Depends(get_db)):
    return sprinkler.Sprinkler.add(session=db, data=data)


@app.delete('/sprinkler/delete/{id}', tags=["sprinkler"])
def delete_sprinkler(id: int, db: Session = Depends(get_db)):
    return sprinkler.Sprinkler.delete(session=db, id=id)


############## SPRINKLER END

############## PLANT

@app.get('/plant/list', response_model=List[Plant], tags=["plant"])
def list_plant(db: Session = Depends(get_db)):
    return plant.Plant.list_all(session=db)


@app.get('/plant/get/{id}', response_model=Plant, tags=["plant"])
def get_plant(id: int, db: Session = Depends(get_db)):
    return plant.Plant.find_by_id(session=db, id=id)


@app.post('/plant/update', response_model=Plant, tags=["plant"])
def update_plant(data: PlantEdit, db: Session = Depends(get_db)):
    return plant.Plant.update(session=db, data=data)


@app.put('/plant/create', response_model=Plant, tags=["plant"])
def create_plant(data: PlantAdd, db: Session = Depends(get_db)):
    return plant.Plant.add(session=db, data=data)


@app.delete('/plant/delete/{id}', tags=["plant"])
def delete_plant(id: int, db: Session = Depends(get_db)):
    return plant.Plant.delete(session=db, id=id)


############## PLANT END

############## WATER-DAY

@app.get('/water-day/list', response_model=List[WaterDay], tags=["water-day"])
def list_water_day(db: Session = Depends(get_db)):
    return waterday.WaterDay.list_all(session=db)


@app.get('/water-day/get/{id}', response_model=WaterDay, tags=["water-day"])
def get_water_day(id: int, db: Session = Depends(get_db)):
    return waterday.WaterDay.find_by_id(session=db, id=id)


@app.post('/water-day/update', response_model=WaterDay, tags=["water-day"])
def update_water_day(data: WaterDayEdit, db: Session = Depends(get_db)):
    return waterday.WaterDay.update(session=db, data=data)


@app.put('/water-day/create', response_model=WaterDay, tags=["water-day"])
def create_water_day(data: WaterDayAdd, db: Session = Depends(get_db)):
    return waterday.WaterDay.add(session=db, data=data)


@app.delete('/water-day/delete/{id}', tags=["water-day"])
def delete_water_day(id: int, db: Session = Depends(get_db)):
    return waterday.WaterDay.delete(session=db, id=id)


############## WATER-DAY END


############## LOG

@app.get('/log/list', response_model=List[Log], tags=["log"])
def list_log(db: Session = Depends(get_db)):
    return log.Log.list_all(session=db)


@app.get('/log/get', response_model=Log, tags=["log"])
def get_log(db: Session = Depends(get_db)):
    return log.Log.find_by_id(session=db, id=id)



@app.put('/log/create', response_model=Log, tags=["log"])
def create_log(data: LogAdd, db: Session = Depends(get_db)):
    return log.Log.add(session=db, data=data)


############## LOG END


