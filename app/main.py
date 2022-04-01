from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

#importing models
from app.models.sensor import Sensor
from app.models.sprinkler import Sprinkler
from app.models.plant import Plant
from app.models.waterday import WaterDay
from app.models.log import(
    Log,
    LogType
)

#importing schemas
from app.models.schemas.sensor import Sensor
from app.models.schemas.sprinkler import Sprinkler
from app.models.schemas.plant import Plant
from app.models.schemas.waterday import WaterDay
from app.models.schemas.log import(
    Log,
    LogType
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


# @app.get("/")
# def main():
#     return RedirectResponse(url="/docs/")


#ROUTES

############## SENSORS

@app.get('/sensor/list', tags=["sensor"])
def list_sensor(db: Session = Depends(get_db)):
    return 0


@app.get('/sensor/get', tags=["sensor"])
def get_sensor(db: Session = Depends(get_db)):
    return 0


@app.post('/sensor/update', tags=["sensor"])
def update_sensor(db: Session = Depends(get_db)):
    return 0


@app.put('/sensor/create', tags=["sensor"])
def create_sensor(sensor_data:Sensor, db: Session = Depends(get_db)):
    return 0


@app.delete('/sensor/delete', tags=["sensor"])
def delete_sensor(db: Session = Depends(get_db)):
    return 0


############## SENSORS END

############## SPRINKLER

@app.get('/sprinkler/list', tags=["sprinkler"])
def list_sprinkler(db: Session = Depends(get_db)):
    return 0


@app.get('/sprinkler/get', tags=["sprinkler"])
def get_sprinkler(db: Session = Depends(get_db)):
    return 0


@app.post('/sprinkler/update', tags=["sprinkler"])
def update_sprinkler(db: Session = Depends(get_db)):
    return 0


@app.put('/sprinkler/create', tags=["sprinkler"])
def create_sprinkler(data: Sprinkler, db: Session = Depends(get_db)):
    return 0


@app.delete('/sprinkler/delete', tags=["sprinkler"])
def delete_sprinkler(db: Session = Depends(get_db)):
    return 0


############## SPRINKLER END

############## PLANT

@app.get('/plant/list', tags=["plant"])
def list_plant(db: Session = Depends(get_db)):
    return 0


@app.get('/plant/get', tags=["plant"])
def get_plant(db: Session = Depends(get_db)):
    return 0


@app.post('/plant/update', tags=["plant"])
def update_plant(db: Session = Depends(get_db)):
    return 0


@app.put('/plant/create', tags=["plant"])
def create_plant(data: Plant, db: Session = Depends(get_db)):
    return 0


@app.delete('/plant/delete', tags=["plant"])
def delete_plant(db: Session = Depends(get_db)):
    return 0


############## PLANT END

############## WATER-DAY

@app.get('/water-day/list', tags=["water-day"])
def list_water_day(db: Session = Depends(get_db)):
    return 0


@app.get('/water-day/get', tags=["water-day"])
def get_water_day(db: Session = Depends(get_db)):
    return 0


@app.post('/water-day/update', tags=["water-day"])
def update_water_day(db: Session = Depends(get_db)):
    return 0


@app.put('/water-day/create', tags=["water-day"])
def create_water_day(data: WaterDay, db: Session = Depends(get_db)):
    return 0


@app.delete('/water-day/delete', tags=["water-day"])
def delete_water_day(db: Session = Depends(get_db)):
    return 0


############## WATER-DAY END


############## LOG

@app.get('/log/list', tags=["log"])
def list_log(db: Session = Depends(get_db)):
    return 0


@app.get('/log/get', tags=["log"])
def get_log(db: Session = Depends(get_db)):
    return 0



@app.put('/log/create', tags=["log"])
def create_log(data: Log, db: Session = Depends(get_db)):
    return 0


@app.delete('/log/delete', tags=["log"])
def delete_log(db: Session = Depends(get_db)):
    return 0


############## LOG END




# @app.get("/records/", response_model=List[schemas.Record], tags=["kkkk"])
# def show_records(db: Session = Depends(get_db)):
#     records = db.query(models.Record).all()
#     return records


# @app.get("/records/{id}", response_model=schemas.Record, tags=["uehuehe", "kkkk"])
# def show_record(id: int, db: Session = Depends(get_db)):
#     """
#     Get record by id
#     """
#     return models.Record.find_by_id(session=db, id=id)
    


# @app.post("/records/{date}/{country}/{cases}/{deaths}/{recoveries}", response_model=schemas.Record)
# def add_record(country: str, cases: int, deaths: int, recoveries: int, db: Session = Depends(get_db)):
#     id = models.Record.add(session=db, date=datetime.now(), country=country, cases=cases, deaths=deaths, recoveries=recoveries)
#     return id
