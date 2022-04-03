import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


#sprinkler
@pytest.mark.order(1)
def test_create_sprinkler(test_create):
    response = test_create.put("/sprinkler", json={
            "description": "test_sprinkler_01",
            "active": True
        }
    )
    assert response.status_code == 201


@pytest.mark.order(1)
def test_create_sprinkler_wrong_value(test_create):
    response = test_create.put("/sprinkler", json={
            "description": "test_sprinkler_01_wrong_value",
            "active": 3
        }
    )
    assert response.status_code == 422



#plant
@pytest.mark.order(1)
def test_create_plant(test_create):
    response = test_create.put("/plant", json={
            "description": "test_plant_01",
            "sprinkler_id": 1,
            "active": True
        }
    )
    assert response.status_code == 201

@pytest.mark.order(1)
def test_create_plant_inexist_sprinkler_id(test_create):
    response = test_create.put("/plant", json={
            "description": "test_plant_01_wrong_id",
            "sprinkler_id": 0,
            "active": True
        }
    )
    assert response.status_code == 400

@pytest.mark.order(1)
def test_create_plant_wrong_value(test_create):
    response = test_create.put("/plant", json={
            "description": "test_plant_01_wrong_value",
            "sprinkler_id": 1,
            "active": 3
        }
    )
    assert response.status_code == 422


#water day
@pytest.mark.order(1)
def test_create_waterday(test_create):
    response = test_create.put("/waterday", json={
            "week_day": 0,
            "time_day": "12:30",
            "water_time": 50,
            "plant_id": 1,
            "active": True
        }
    )
    assert response.status_code == 201


@pytest.mark.order(1)
def test_create_waterday_wrong_week_day(test_create):
    response = test_create.put("/waterday", json={
            "week_day": 7,
            "time_day": "12:30",
            "water_time": 50,
            "plant_id": 1,
            "active": True
        }
    )
    assert response.status_code == 400
    assert response.json()["message"] == "Weekday must be between 0-6 (0: Monday/6: Sunday)"
    assert response.json()["exception"] == "Weekday 7 is invalid"


@pytest.mark.order(1)
def test_create_waterday_wrong_time_day(test_create):
    response = test_create.put("/waterday", json={
            "week_day": 0,
            "time_day": "1c:30",
            "water_time": 50,
            "plant_id": 1,
            "active": True
        }
    )
    assert response.status_code == 400
    assert response.json()["message"] == "Time Day must be in format HH:MM - 24 format"
    assert response.json()["exception"] == "time data '1c:30' does not match format '%H:%M'"



@pytest.mark.order(1)
def test_create_waterday_wrong_value_timeday(test_create):
    response = test_create.put("/waterday", json={
            "week_day": 0,
            "time_day": "12:30",
            "water_time": 'a',
            "plant_id": 1,
            "active": True
        }
    )
    assert response.status_code == 422
    

@pytest.mark.order(1)
def test_create_waterday_inextis_plant_id(test_create):
    response = test_create.put("/waterday", json={
            "week_day": 0,
            "time_day": "12:30",
            "water_time": 50,
            "plant_id": 0,
            "active": True
        }
    )
    assert response.status_code == 400
    assert response.json()["message"] == "Don't find plant_id specified"
    assert response.json()["exception"] == "plant_id 0 not found"




#log
@pytest.mark.order(1)
def test_create_log(test_create):
    response = test_create.put("/log", json={
            "plant_id": 1,
            "key": "OK"
        }
    )
    assert response.status_code == 201


@pytest.mark.order(1)
def test_create_log_inextis_plant_id(test_create):
    response = test_create.put("/log", json={
            "plant_id": 0,
            "key": "OK"
        }
    )
    assert response.status_code == 400
    assert response.json()["message"] == "Don't find plant_id specified"
    assert response.json()["exception"] == "plant_id 0 not found"


@pytest.mark.order(1)
def test_create_log_wrong_key(test_create):
    response = test_create.put("/log", json={
            "plant_id": 1,
            "key": "WRONG"
        }
    )
    assert response.status_code == 400
    assert response.json()["message"] == "Key must be OK or FAIL"
    assert response.json()["exception"] == "Unrecognized key data"
