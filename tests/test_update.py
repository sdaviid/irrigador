import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


#sprinkler
@pytest.mark.order(3)
def test_update_sprinkler(test_update):
    response = test_update.post("/sprinkler/update", json={
        "id": 1,
        "description": "test_sprinkler_01_updated",
        "active": True
        }
    )
    assert response.status_code == 200


@pytest.mark.order(3)
def test_update_sprinkler_inexist_id(test_update):
    response = test_update.post("/sprinkler/update", json={
        "id": 0,
        "description": "test_sprinkler_01_updated",
        "active": True
        }
    )
    assert response.status_code == 404
    assert response.json()["message"] == "Don't find ID specified"


@pytest.mark.order(3)
def test_update_sprinkler_wrong_value(test_update):
    response = test_update.post("/sprinkler/update", json={
        "id": 1,
        "description": "test_sprinkler_01_updated",
        "active": 3
        }
    )
    assert response.status_code == 422



#plant
@pytest.mark.order(3)
def test_update_plant(test_update):
    response = test_update.post("/plant/update", json={
            "id": 1,
            "description": "test_plant_01_updated",
            "sprinkler_id": 1,
            "active": True
        }
    )
    assert response.status_code == 200


@pytest.mark.order(3)
def test_update_plant_inexist_id(test_update):
    response = test_update.post("/plant/update", json={
            "id": 0,
            "description": "test_plant_01_updated",
            "sprinkler_id": 1,
            "active": True
        }
    )
    assert response.status_code == 404
    assert response.json()["message"] == "Don't find ID specified"


@pytest.mark.order(3)
def test_update_plant_inexist_sprinkler_id(test_update):
    response = test_update.post("/plant/update", json={
            "id": 1,
            "description": "test_plant_01_updated_wrong_sprinkler_id",
            "sprinkler_id": 0,
            "active": True
        }
    )
    assert response.status_code == 400


@pytest.mark.order(3)
def test_update_plant_wrong_value(test_update):
    response = test_update.post("/plant/update", json={
            "id": 1,
            "description": "test_plant_01_updated_wrong_value",
            "sprinkler_id": 1,
            "active": 3
        }
    )
    assert response.status_code == 422



#water day
@pytest.mark.order(3)
def test_update_waterday(test_update):
    response = test_update.post("/waterday/update", json={
            "id": 1,
            "week_day": 0,
            "time_day": "12:30",
            "water_time": 50,
            "plant_id": 1,
            "active": True
        }
    )
    assert response.status_code == 200


@pytest.mark.order(3)
def test_update_waterday_indexist_id(test_update):
    response = test_update.post("/waterday/update", json={
            "id": 0,
            "week_day": 0,
            "time_day": "12:30",
            "water_time": 50,
            "plant_id": 1,
            "active": True
        }
    )
    assert response.status_code == 404
    assert response.json()["message"] == "Don't find ID specified"



@pytest.mark.order(3)
def test_update_waterday_wrong_week_day(test_update):
    response = test_update.post("/waterday/update", json={
            "id": 1,
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


@pytest.mark.order(3)
def test_update_waterday_wrong_time_day(test_update):
    response = test_update.post("/waterday/update", json={
            "id": 1,
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



@pytest.mark.order(3)
def test_update_waterday_wrong_value_timeday(test_update):
    response = test_update.post("/waterday/update", json={
            "id": 1,
            "week_day": 0,
            "time_day": "12:30",
            "water_time": 'a',
            "plant_id": 1,
            "active": True
        }
    )
    assert response.status_code == 422
    

@pytest.mark.order(3)
def test_update_waterday_inextis_plant_id(test_update):
    response = test_update.post("/waterday/update", json={
            "id": 1,
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